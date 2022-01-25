#include<stdio.h>
#include<iostream>
#include<math.h>
#include<vector>
#include<iomanip>
#include<fstream>

using namespace std;

double long G = 6.67e-11;
ofstream myfile;

vector<long double>  vecSub(vector<long double> a, vector<long double> b){
	long n = a.size();
	vector<long double> res(n);
	for(int i = 0; i < n; i++) {res[i] = a[i] - b[i];}
	return res; 
}

vector<long double> constVecMult(long double x, vector<long double> v)
{
	long n = v.size();
	vector<long double> res(n);
	for(int i = 0; i < n; i++) {res[i] = x*v[i];}
	return res;
}

vector<long double> vecSum(vector<long double> a, vector<long double> b)
{
	long n = a.size();
	vector<long double> res(n);
	for(int i = 0; i <n; i++) {res[i] = a[i] + b[i];}
	return res;
}

class Particle
{
	public:
	long double mass;
	vector<long double> pos;
	vector<long double> vel;

	Particle(long double m, vector<long double> p, vector<long double> v) {
		mass = m;
		pos = p;
		vel = v;
	}
	
	void printPos()
	{
		cout << fixed << pos[0] << ",\t" << pos[1] <<",\t"<< pos[2] << endl;
	}
	
	void printMass()
	{
		cout << mass << endl;
	}

	void printVel()
	{
		cout << vel[0] << ",\t" << vel[1] <<",\t"<< vel[2] << endl;
	}
	vector<long double> u(Particle p_j)
	{
		return vecSub(p_j.pos,pos);
	}
};


class Container
{
	public:
	vector<Particle> particles;

	Container(vector<Particle> parts)
	{
		particles = parts;
	}
	
	void printPos()
	{
		for(long i = 0; i < particles.size(); i++)
			particles[i].printPos();
	}
	
	void writePos()
	{
		for(long i = 0; i < particles.size(); i++)
		{
			myfile << fixed <<particles[i].pos[0] <<"\t" <<particles[i].pos[1] <<"\t" << particles[i].pos[2] << endl;
		}
	}

};

class Integrator
{
	public:
	long M;
	double dt;

	Integrator(double deltaT,long  n)
	{
		dt = deltaT;
		M = n;
	}

	Container riemman(Container container)
	{
		for(long j = 0; j < M; j++)
		{
			Particle p_j = container.particles[j];
			for(long i = 0; i < M; i++)
			{
				if(i == j) {continue;}
				Particle p_i = container.particles[i];
				vector<long double> u = p_j.u(p_i);
				
				//cout << "u = " << u[0] <<","<<u[1]<<","<<u[2] << endl;
				long double r = sqrt(u[0]*u[0] + u[1]*u[1] + u[2]*u[2]);
				long double C = (G*p_j.mass * p_i.mass / (pow(r,3)));
				vector<long double> F = constVecMult(C,u);
				
				//cout << "F = " << F[0] <<", " << F[1] << " " << F[2]<<endl; 
				vector<long double> V = constVecMult(dt/p_j.mass, F);


				//cout << "V =" << V[0] << " " << V[1] << " " << V[2] << endl;
				container.particles[j].vel = vecSum(container.particles[j].vel, V); 
				//cout << "VEL = ";
				//container.particles[j].printVel();
			}
		}

		for(int j = 0; j < M; j++)
		{
			
			Particle p_j = container.particles[j];
			vector<long double> aux = vecSum(p_j.pos,constVecMult(dt,p_j.vel));
			vector<long double> aux1 = constVecMult(dt,p_j.vel);
			//cout << "dt =" << dt << endl;
			//cout << "vel = " <<p_j.vel[0] << " " << p_j.vel[1] << " " << p_j.vel[2] << endl;
			//cout << "vel: ";
			//p_j.printVel();
			//cout << "dt: " << dt << endl;
			//cout << "dt*vel = " << aux[0] << ","<<aux[1]<<","<<aux[2]<<endl;
			container.particles[j].pos = vecSum(p_j.pos,constVecMult(dt,p_j.vel));
			//cout << "pos = " << container.particles[j].pos[0] << " " << container.particles[j].pos[1] << " " << container.particles[j].pos[2] << endl;
		}
		
		return container;
	}
};

int main() 
{	
	//ofstream myfile;
	double dt = 86400/4; // 1 day = 86400s
	long M;
	long N = 365*165*2;//3.6*24*365;

	long double mass, x, y, z, vx, vy, vz;
	string name;

	vector<string> names;
	vector<Particle> system;

	cin >> M;
	//N particles, name,  mass, X, Y, Z, Vx, Vy, Vz
	for(int i = 0; i < M; i++)
	{
		cin >> name >> mass >> x >> y >> z >> vx >> vy >> vz;
		names.push_back(name);
		system.push_back(Particle(mass, {x*1000, y*1000, z*1000}, {vx*1000, vy*1000, vz*1000}));
	}

	Container c1 = Container(system);
	M = system.size();
	c1.printPos();
	Integrator s1 = Integrator(dt,M);
	//cout << ":)" << endl;
	cout << "Performing " << N << "operation " << endl;
	myfile.open("example.txt");

	myfile << M << "\t" <<N<<"\n";

	for(int i = 0; i < N; i++) 
	{
		c1 = s1.riemman(c1);
		//c1.printPos();
		c1.writePos();
	}

	for(auto c: names)
	{
	myfile << c << endl;
	}
	myfile.close();
	return 0;
}
