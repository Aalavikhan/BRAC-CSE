#include<stdio.h>
int main(){
    int a;
    scanf("%d",&a);
    if (a>=1000){
        printf("Money man\n");

        if (a>=5000){
            printf("You rich");
        }
    }

    else if (a>=500){
        printf("motamoti rich");
    }

    else{
        printf("stinky");
    }

    return 0;
}