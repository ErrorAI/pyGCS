#include <iostream>
#include <math.h>
#include <fstream>
#include <string>

#include "cuba.h"

#define clearData
//#define deb
//#define debug

#include "mstwpdf.h"

struct constant_struct
{
  string const_name;
  double const_value;
};

const double PI = 3.141592653589793238462643383279502884197169399375105820974944;

int num_of_kinemat_var;
double* p_kinem_var_min;
double* p_kinem_var_max;
double G_BIN_MIN;
double G_BIN_MAX;

constant_struct* constants;
int num_of_constants;

c_mstwpdf *mstwpdf;

// Wrapper around Fortran code for alpha_S.
extern "C" {
  void initalphas_(int *IORD, double *FR2, double *MUR, double *ASMUR,
		   double *MC, double *MB, double *MT);
  double alphas_(double *MUR);
}
inline void InitAlphaS(int IORD, double FR2, double MUR, double ASMUR,
		       double MC, double MB, double MT) {
  initalphas_(&IORD, &FR2, &MUR, &ASMUR,
	      &MC, &MB, &MT);
}
inline double AlphaS(double MUR) {
  return alphas_(&MUR);
}
//#########################################

//====Функция проверки кинематики
double inline Kinematic(double x, double y, double z, double u, double v, double w){
//    Proverka kinematicheskih parametrov.
//    x==s, y==t, z==m2**2, u==ma**2, v==mb**2, w==m1**2.
//    Imeetsya v vidu process: a+b -> 1+2.
//    (snachala, s kajdoy storonyi, verhnie, potom nijnie).
//      Real*8 Function Kinematic(x,y,z,u,v,w)
//      Implicit Real*8(A-H,K,M,O-Z)
     return ( pow(v,2)*w + pow(u,2)*z - u*(-(w*y) + x*y + w*z + x*z + y*z - pow(z,2) + v*(w - x + z)) + x*(y*(x + y - z) + w*(-y + z)) + v*(pow(w,2) + y*(-x + z) - w*(x + y + z)) );
}
//end=Функция проверки кинематики

static int Integrand(const int *ndim, const cubareal xx[],
  const int *ncomp, cubareal ff[], void *userdata) {

//====Переназначение констант заданных в конфиге	
    double sqrt_s;
    double mu_mult;
    double mass;
    double R0_sqr;
    double q2Tsr;
    for(int i = 0; i < num_of_constants; i++){
        if(constants[i].const_name == "sqrt_s"){sqrt_s = constants[i].const_value;}
        if(constants[i].const_name == "mu_mult"){mu_mult = constants[i].const_value;}
        if(constants[i].const_name == "mass"){mass = constants[i].const_value;}
        if(constants[i].const_name == "R0_sqr"){R0_sqr = constants[i].const_value;}
        if(constants[i].const_name == "q2Tsr"){q2Tsr = constants[i].const_value;}
    }
//end=Переназначение констант заданных в конфиге	
 
    double s = pow(sqrt_s,2);
    double mass2 = pow(mass,2);
    double mass4 = pow(mass,4);


    
    double m_3T = sqrt( pow(q_3T,2)+mass2 );
    
    double xi_1 = exp(y_3)*m_3T/sqrt_s;
    double xi_2 = exp(-y_3)*m_3T/sqrt_s;

    double a = pow(s*x_1,2)-pow(s,2)*x_1*xi_1;
    double b = mass2*s*x_1 - pow(q_1T,2)*s*xi_1 - pow(s*x_1,2)*xi_2 -
                2*q_1T*q_2T*s*x_1*cos(phi_2) +
                2*q_2T*q_3T*s*x_1*cos(phi_3 - phi_2) +
                2*q_1T*q_3T*s*x_1*cos(phi_3);
    double c = pow(q_1T*q_2T,2) - pow(q_2T,2)*s*x_1*xi_2;

    if( (pow(b,2)-4*a*c) <= 0 ){
        ff[0] = 0;
        return 0;
    }

    double x_2 = (-b+sqrt(pow(b,2)-4*a*c))/(2*a);
    
    double Darg = -pow(q_1T*q_2T,2)/(s*x_1*pow(x_2,2))+s*(x_1-xi_1)+
                    pow(q_2T,2)*xi_2/pow(x_2,2);

    if((x_2 <= 0) || (x_2 >= 1)){
    ff[0] = 0;
    return 0;
    }


  double q = m_3T * mu_mult; //Объявление жеского масштаба
  double alpha_s = AlphaS(q); //Рассчет бегущей alpha
  //printf("%.5f %.5f %.5f %.5f %.5f\n", x_1, x_2, m_3T, q, alpha_s);

//====Рассчет партонных функций
  double parton_func_1 = exp(-pow(q_1T,2)/q2Tsr)/(PI*q2Tsr)*mstwpdf->parton(0,x_1,q)/x_1;
  double parton_func_2 = exp(-pow(q_2T,2)/q2Tsr)/(PI*q2Tsr)*mstwpdf->parton(0,x_2,q)/x_2;
//end=Рассчет партонных функций

    //printf("1) %.5f\n",exp(-pow(q_1T,2)/q2Tsr));
    //printf("2) %.5f\n",exp(-pow(q_2T,2)/q2Tsr));
    //printf("3) %.5f\n",exp(-pow(q_1T,2)/0.05));
    //printf("4) %.5f\n",exp(-pow(q_2T,2)/0.05));

    double s_hat = s*x_1*x_2 - 2*q_1T*q_2T*cos(phi_2) + pow(q_1T*q_2T,2)/(s*x_1*x_2);
    double t_hat = mass2 - exp(y_3)*m_3T*pow(q_1T,2)/(sqrt_s*x_1) -
                    exp(-y_3)*m_3T*sqrt_s*x_1 +
                    2*q_1T*q_3T*cos(phi_3);
    double u_hat = mass2 - exp(-y_3)*m_3T*pow(q_2T,2)/(sqrt_s*x_2) -
                    exp(y_3)*m_3T*sqrt_s*x_2 +
                    2*q_2T*q_3T*cos(phi_3-phi_2);

    if(s_hat+t_hat+u_hat-mass2 > 1e-9){
        ff[0] = 0;
        return 0;
    }


    double AA = x_1 * sqrt_s / 2 * m_3T * exp(-y_3) + pow(q_1T,2)*m_3T*exp(y_3)/2/sqrt_s/x_1;
    double BB = x_2 * sqrt_s / 2 * m_3T * exp(y_3) + pow(q_2T,2)*m_3T*exp(-y_3)/2/sqrt_s/x_2;
    double phi_4 = acos( -(mass2+s_hat)/2 + AA + BB ) + phi_3;
    //double secpT = sqrt( pow(q_1T,2) + pow(q_2T,2) + 2*q_1T*q_2T*cos(phi_2) );
    //double e_1 = pow(q_1T,2)/2/sqrt_s/x_1+sqrt_s*x_1/2;
    //double e_2 = pow(q_2T,2)/2/sqrt_s/x_2+sqrt_s*x_2/2;
    //double q_1z = -pow(q_1T,2)/2/sqrt_s/x_1+sqrt_s*x_1/2;
    //double q_2z = pow(q_2T,2)/2/sqrt_s/x_2-sqrt_s*x_2/2;
    //double y_4 = 1/2*log(( e_1 + e_2 - m_3T*exp(y_3) + q_1z + q_2z )/( e_1 + e_2 - m_3T*exp(-y_3) - q_1z - q_2z ));
//====Срез по бину "китайским методом"
  if((q_3T < G_BIN_MIN) || (G_BIN_MAX < q_3T)){
  //if((sqrt(s_hat) < G_BIN_MIN) || (G_BIN_MAX < sqrt(s_hat))){
  //if((abs(phi_3-phi_4) < G_BIN_MIN) || (G_BIN_MAX < abs(phi_3-phi_4))){
  //if((secpT < G_BIN_MIN) || (G_BIN_MAX < secpT)){
  //if(( abs(y_4-y_3) < G_BIN_MIN ) || ( G_BIN_MAX < abs(y_4-y_3) )){
    ff[0] = 0;
    return 0;
  } 
//end=Срез по бину "китайским методом"


if( s_hat < pow(sqrt( mass2 + pow(p_kinem_var_min[1],2)) /*+ pow(p_kinem_var_min[1],2)*/,2)){                                                                                    
   ff[0] = 0;
   return 0;
   } 
//====Рассчет матричного элемента
/* double sqr_M = pow(4.0*PI*alpha_s,2)*((4.0*mass4-mass2*s_hat)/((mass2-t_hat)*
	(mass2-u_hat))+9.0*(mass4+mass2*(s_hat-2.0*u_hat)+pow(u_hat,2))/
	(s_hat*(mass2-u_hat))-18.0*(mass4+pow(s_hat,2)+mass2*(s_hat-2.0*
	u_hat)+s_hat*u_hat+pow(u_hat,2))/pow(s_hat,2)-4.0*(3.0*mass4-mass2*s_hat+
	u_hat*(s_hat+u_hat))/pow((mass2-u_hat),2)+9.0*(mass4+pow(s_hat+u_hat,2)-
	mass2*(s_hat+2.0*u_hat))/(s_hat*(mass2-t_hat))-4.0*(7.0*
	mass4+u_hat*(s_hat+u_hat)-mass2*(3.0*s_hat+4.0*u_hat))/
	pow((mass2-t_hat),2))/24;
*/
/*  double OC3S1 = 1.3;
  double sqr_M = pow(PI,3) * pow(alpha_s,3) * OC3S1 / (mass * mass2) * (320 * mass4)/(81 * pow(mass2 - t_hat,2) * pow(mass2 - u_hat,2) * pow(t_hat + u_hat,2)) * (mass4*pow(t_hat,2) - 2*mass2*pow(t_hat,3) + pow(t_hat,4) + mass4*t_hat*u_hat - 3*mass2*pow(t_hat,2)*u_hat + 2*pow(t_hat,3)*u_hat + mass4*pow(u_hat,2) - 3*mass2*t_hat*pow(u_hat,2) + 3*pow(t_hat,2)*pow(u_hat,2) - 2*mass2*pow(u_hat,3) + 2*t_hat*pow(u_hat,3) + pow(u_hat,4));
*/
  double sqr_M = 16 * PI * pow(s_hat,2) * (5*PI*pow(alpha_s,3)*R0_sqr*mass)/(9*pow(s_hat,2))*( pow(s_hat,2)/(pow(t_hat-mass2,2)*pow(u_hat-mass2,2)) + pow(t_hat,2)/(pow(u_hat-mass2,2)*pow(s_hat-mass2,2)) + pow(u_hat,2)/(pow(s_hat-mass2,2)*pow(t_hat-mass2,2)) );
 //double sqr_M = 1; 
 //====Проверка матричного, что он > 0
  if(sqr_M < 0){
  ff[0] = 0;
  return 0;
  }
  //end=Проверка матричного, что он > 0
//end=Рассчет матричного элемента

//====Сечение и его пересчет
  double dsigma_tilde = (q_1T * q_2T * q_3T * sqr_M)/(8 * PI * Darg * s_hat);
  ff[0] = dsigma_tilde * 0.38938e6 * parton_func_1 * parton_func_2 * jacob / (G_BIN_MAX - G_BIN_MIN);

  //Перевод в сечение Br/(2 pi p_T)*(dG/(dp_T dy)), зависимость от p_T
  ff[0] = ff[0] * 0.06 / ( /*2 * PI **/ q_3T ) / ( p_kinem_var_max[0] - p_kinem_var_min[0] );
//end=Сечение и его пересчет
  //printf("------\n");
  //printf("%.5f %.5f\n",pow(b,2),-4*a*c);
  //printf("%.5f\n",x_2);
  //printf("%.5f %.5f %.5f %.5f %.5f %.5f\n", sqr_M, Darg, J, s_hat, t_hat, u_hat);
  //printf("%.5f %.5f %.5f\n", parton_func_1 , parton_func_2 , jacob);
  //printf("------");
  return 0;
}


//====Параметры для интегратора
#define NDIM 7
#define NCOMP 1
#define USERDATA NULL
#define NVEC 1
#define EPSREL 5e-2
#define EPSABS 1e-19
#define VERBOSE 0
#define LAST 4
#define SEED 22
#define MINEVAL 0
#define MAXEVAL 2e9 //5e7
#define STATEFILE NULL
#define SPIN NULL
#define NNEW 24e4
#define NMIN 8e4 //3e4
#define FLATNESS 1e0
//end=Параметры для интегратора

int main(int argc, char *argv[]){

#ifndef clearData
  cout << "\n\n\n\n=====================================" << endl;
  cout << "!!!!!=====Start computation=====!!!!!" << endl;
  cout << "=====================================" << endl;
#endif

//====Инициализация бегущей константы alpha
double alphaSorder = 0.0;
double alphaSQ0 = 0.68183;
double alphaSMZ = 0.13939;
double mCAS = 1.4;
double mBAS = 4.75;
double mTAS = 1.0e10;
InitAlphaS(alphaSorder,1.0,1.0,alphaSQ0,
mCAS,mBAS,mTAS);
//end=Инициализация бегущей константы alpha

//====Объявление пути к таблицам партонных функций  
char filename[100];
char prefix[] = "mstwGrids/mstw2008lo";
sprintf(filename,"%s.%2.2d.dat",prefix,0);
mstwpdf = new c_mstwpdf(filename);
//end=Объявление пути к таблицам партонных функций  

//====Блок считывания файла настроек
int num_of_bins;
double* p_bins;
std::ifstream conf_file_in (argv[1]);
if (conf_file_in.is_open()){
#ifndef clearData
std::cout << "Using ( " << argv[1] << " ) config file" << std::endl;
#endif
}else{
std::cout << "Config file ( " << argv[1] << " ) not open" << std::endl;
return -1;
}
std::string line;
int temp_ind_1;
int temp_ind_2;
std::string conf_param;
std::string conf_arg;
while(getline(conf_file_in, line)){
temp_ind_1 = line.find(' ');
while(temp_ind_1 != -1){
line.erase(temp_ind_1, 1);
temp_ind_1 = line.find(' ');
}
temp_ind_1 = line.find("(");
temp_ind_2 = line.rfind(")");
conf_param = line.substr(0, temp_ind_1 );
conf_arg = line.substr(temp_ind_1 + 1, temp_ind_2 - temp_ind_1 - 1);  
//    cout << conf_param << "\t==\t" << conf_arg << endl; //debug
if( conf_param == "constants"){
temp_ind_1 = conf_arg.find("|");
num_of_constants = stoi( conf_arg.substr(0,temp_ind_1) );
constants = new constant_struct[num_of_constants];
conf_arg = conf_arg.substr(temp_ind_1 + 1);

for(int i = 0; i < num_of_constants; i++){
temp_ind_1 = conf_arg.find("{");
temp_ind_2 = conf_arg.find("}");
constants[i] = { conf_arg.substr(0, temp_ind_1), stod( conf_arg.substr(temp_ind_1 + 1, temp_ind_2 - temp_ind_1 - 1) ) };
conf_arg = conf_arg.substr(temp_ind_2 + 1);
}
}
if( conf_param == "kinem_var"){
temp_ind_1 = conf_arg.find("|");
num_of_kinemat_var = stoi( conf_arg.substr(0, temp_ind_1) );
p_kinem_var_min = new double [num_of_kinemat_var];
p_kinem_var_max = new double [num_of_kinemat_var];
conf_arg = conf_arg.substr(temp_ind_1 + 1);
for(int i = 0; i < num_of_kinemat_var; i++){
temp_ind_1 = conf_arg.find("{");
temp_ind_2 = conf_arg.find(",");
p_kinem_var_min[i] = stod( conf_arg.substr(temp_ind_1 + 1, temp_ind_2 - temp_ind_1 - 1) );
temp_ind_1 = conf_arg.find("}");
p_kinem_var_max[i] = stod( conf_arg.substr(temp_ind_2 + 1, temp_ind_1 - temp_ind_2 - 1) );
conf_arg = conf_arg.substr(temp_ind_1 + 1);
}
}
if( conf_param == "bins"){
if( conf_arg.substr(0, 1) == "f" ){
string bin_file = conf_arg.substr(2);
std::ifstream bin_file_in (bin_file);
if (bin_file_in.is_open()){
  #ifndef clearData
	std::cout << "Using ( " << bin_file << " ) bin file" << std::endl;
  #endif
}else{
  std::cout << "Config file ( " << bin_file << " ) not open" << std::endl;
  return -1;
}
string bin_line;
getline(bin_file_in, bin_line);
num_of_bins = stoi( bin_line );
p_bins = new double [num_of_bins];
int i = 0;
while(getline(bin_file_in, bin_line)){
  p_bins[i] = stod( bin_line );
  i++;
}
bin_file_in.close();
}else{
temp_ind_1 = conf_arg.find("|");
temp_ind_2 = conf_arg.rfind("|");
num_of_bins = stoi( conf_arg.substr(0, temp_ind_1) );
double start_bin = stod( conf_arg.substr(temp_ind_1 + 1, temp_ind_2 - temp_ind_1 - 1) );
double step_bin = stod( conf_arg.substr(temp_ind_2 + 1) );
p_bins = new double [num_of_bins];
for(int i = 0; i < num_of_bins; i++){
  p_bins[i] = start_bin + i * step_bin;
}
}
}
}
conf_file_in.close();
//end=Блок считывания файла настроек

//====Вывод считанных данных файла настроек
#ifndef clearData
cout << "==========Config_Parameters==========" << endl;
cout << "num_of_bins\t=\t" << num_of_bins << endl;
cout << "-----Bins-----" << endl;
for(int i = 0; i < num_of_bins; i++){
cout << "p_bins[" << i << "]\t=\t" << p_bins[i] << endl;
}
cout << "--------------" << endl;
cout << "---Kinem_var--" << endl;
cout << "num_of_kinemat_var\t=\t" << num_of_kinemat_var << endl;
for(int i = 0; i < num_of_kinemat_var; i++){
cout << "p_kinem_var_min[" << i << "]\t=\t" << p_kinem_var_min[i] << endl;
cout << "p_kinem_var_max[" << i << "]\t=\t" << p_kinem_var_max[i] << endl;
}
cout << "---Constants--" << endl;
for(int i = 0; i < num_of_constants; i++){
cout << constants[i].const_name << "\t" << constants[i].const_value << endl;
}
cout << "=====================================" << endl;
#endif
//end=Вывод считанных данных файла настроек

//====Запуск интегратора по бинам
int nregions, neval, fail;
cubareal integral[NCOMP], error[NCOMP], prob[NCOMP];

for(int i = 0; i < num_of_bins - 1 ; i++){
G_BIN_MIN = p_bins[i];
G_BIN_MAX = p_bins[i+1];

Suave(NDIM, NCOMP, Integrand, USERDATA, NVEC,
EPSREL, EPSABS, VERBOSE | LAST, SEED,
MINEVAL, MAXEVAL, NNEW, NMIN, FLATNESS,
STATEFILE, SPIN, &nregions, &neval, &fail, integral, error, prob);

printf("%.3f \t%.3f \t%.20f \t%.8f \t%.3f\n",G_BIN_MIN,G_BIN_MAX,(double)integral[0], (double)error[0]/(double)integral[0]*100,(double)prob[0]);
}
cout << "\n\n" << endl;
delete [] p_kinem_var_min;
delete [] p_kinem_var_max;
delete [] p_bins;
//====Запуск интегратора по бинам

}
