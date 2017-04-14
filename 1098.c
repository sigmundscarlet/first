#include<stdio.h>
int main()
{
    int n,tot=0,sum=0,card[106],i;
    scanf("%d",&n);
    for(i=1;i<=n;i++)
    {       
        scanf("%d",&card[i]);
        sum+=card[i];
    }
    sum/=n;
    for(i=1;i<=n;i++)
    {
        card[i]-=sum;
    }
    for(i=1;i<=n;i++)
    {
        if(!card[i])continue;
        card[i+1]+=card[i];
        card[i]=0;
        tot++;
    }
    printf("%d\n",tot);
    return 0;
}
