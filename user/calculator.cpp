/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>

using namespace std;
add(int x,int y)
{
    int a;
    a=x+y;
    return a;
}
multiply(int x,int y)
{
     int a;
    a=x*y;
    return a;
}
minus(int x,int y)
{
     int a;
    a=x-y;
    return a;
}
divide(int x,int y)
{
     int a;
    a=x/y;
    return a;
}
int main()
{
    //cout<<"Hello World";
string str;
cin>>str;
int x,y;
cin>>x>>y;
if(str==add)
{
int z=add(x,y);
cout<<z;
}

if(str==divide)
{
int z=divide(x,y);
cout<<z;
}if(str==multiply)
{
int z=multiply(x,y);
cout<<z;
}

if(str==minus)
{
int z=minus(x,y);
cout<<z;
}
    return 0;
}
