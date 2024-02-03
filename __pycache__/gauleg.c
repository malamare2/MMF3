#include <stdio.h> 
#include <math.h>
#include <malloc.h>
#include <stdlib.h>

void gauleg(float x1, float x2, float x[], float w[], int n)
//Given the lower and upper limits of integration x1 and x2, and given n, this routine returns arrays x[1..n] and w[1..n] of length n, containing the abscissas and weights of the Gauss-Legendre n-point quadrature formula. 
// ulazni parametri gdje imamo gornju i donju granicu integracije, n je stupanj legendrovog polinoma
// x traži nultočke a w zapisujemo pripadne težine
{
        double EPS=0.000001;	
	int m,j,i;
	double z1,z,xm,xl,pp,p3,p2,p1;
//definiraju se varijable koje ce se koristiti
	m=(n+1)/2;
// #brojac jer trazimo samo pola jer su simetricne ostale nultocke s obzirom na nulu pa nije potrebno gledat obe strane
       xm=0.5*(x2+x1); //brojac
// sredina intervala
       xl=0.5*(x2-x1);
// pola duljine intervala
//pomocu xm i xl tocke se legendrovog polinoma pozicioniraju na traženi interval[x1, x2]
  	for (i=1;i<=m;i++) 
      {
//brojac koji se koristi
// petlja koja pomaze pri odredivanju nultocki
	z=cos(3.141592654*(i-0.25)/(n+0.5));
//newton rapsonova metoda
  do {
//pomocu relacije se odabire pocetna vrijednost
	p1=1.0;
	p2=0.0;
// legendrovi polinomi te njihove pocetne vrijednosti za prva dva
	for (j=1;j<=n;j++) {
        p3=p2;
	p2=p1;
// 
	p1=((2.0*j-1.0)*z*p2-(j-1.0)*p3)/j;
	}    
// kako se svi iduci dobiju

	pp=n*(z*p1-p2)/(z*z-1.0);
// derivacija legendrovog polinoma
	z1=z;
	z=z1-p1/pp;  
//z je nultocka koja se pronade u petlji
   } while (fabs(z-z1) > EPS);
//  vrijedi kad je nultocka veca od epsilona(pozitivna)
	x[i]=xm-xl*z;
	x[n+1-i]=xm+xl*z;
// upisuju se u listu nultocke
	w[i]=2.0*xl/((1.0-z*z)*pp*pp);
	w[n+1-i]=w[i];

       } // racunanje tezine
  
}



