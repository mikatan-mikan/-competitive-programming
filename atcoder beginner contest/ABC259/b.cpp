#include <iostream>
#include <math.h>

int main(){
    long double e,f,g;
    std::cin >> e >> f >> g;
    long double a = (long double)e;
    long double b = (long double)f;
    long double d = (long double)g;
    long double PI = 3.141592653589793238462643383279502884197169399375105820974944;
    long double b_ra = (long double)d * PI / 180.0;
    long double X = (long double)a * cos(b_ra) - (long double)b * sin(b_ra);
    long double Y = (long double)b * cos(b_ra) - (long double)a * sin(b_ra);

    std::cout << X << " " << Y ;
}