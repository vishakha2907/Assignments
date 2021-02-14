#include<iostream>
using namespace std;
void calculate(int r1,int r2,int c1,int c2){
int i, j, arr1[100][100],
              arr2[100][100],
              arr3[100][100];
              if(r1 <=0 || r2 <=0|| c1<=0 || c2<=0 )
                cout<<"invalid input"<<endl;
                else if(r1 > 1000 || r2 >1000 || c1>1000 || c2>1000)
                    cout<<"out of range ";
              else {
 cout<<"Enter the elements of first matrix \n";
    for(i = 0; i < r1; i++)
    {
        for(j = 0; j < c1; j++)
        {
            cin>>arr1[i][j];
        }
    }
    cout<<"\nEnter the elements of second matrix";
    for(i = 0; i < r2; i++)
        {
        for(j = 0; j < c2; j++)
        {
            cin>>arr2[i][j];
        }
    }
    printf("\narr1 * arr2 = ");
    for(i = 0; i < r1; i++)
    {
        for(j = 0; j < c2; j++)
        {
            arr3[i][j] = 0;
             for(int k = 0; k < c1; k++)
            {
                arr3[i][j] += arr1[i][k] * arr2[k][j];
            }
        }
        printf("\n");
    }
    for(i = 0; i < r2; i++)
    {
        for(j = 0; j < c2; j++)
        {
            printf("%d ", arr3[i][j]);
        }
        printf("\n");
    }
              }
}
int main()
{
    int r1;
    int r2;
    int c1;
    int c2;
              cout<<"Enter the row and column values for the first matrix ";
              cin>>r1>>c1;
              cout<<"Enter the row and column values for the second matrix ";
              cin>>r2>>c2;

    calculate(r1,r2,c1,c2);
    return 0;
}
