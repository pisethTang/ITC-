#include <iostream>
#include <iomanip>
#include <conio.h>
#include <cstring>
#include<cstdio>
#include<cstdlib>
using namespace std;

class LinkedList
{
private:
    struct saver
    {
        char pname[30]; //Product name
        int pid;    //Product id
        int price;    //Product price
        int tquant; //Total products purchased from wholesale
        int aquant; //How many are available in stock
        int rack;   //Rack number where product is stored
    };
    struct saver s;
    struct node
    {
        char pname[30]; //Product name
        int pid;    //Product id
        int price;    //Product price
        int tquant; //Total products purchased from wholesale
        int aquant; //How many are available in stock
        int rack;   //Rack number where product is stored
        struct node *link;
    };

    typedef struct node *nodeptr;   //nodeptr is a user-defined
    //data-type of type struct node *

    nodeptr H;

public:
    LinkedList();   //Constructor
    ~LinkedList();  //Destructor
    struct node * get_node()     //Create a new node
    {
        return (new node);
    }
    int getcount();
    void add_front(char [] , int , int , int , int , int );
    void add_end(char [], int , int , int , int , int );
    void add_middle(int,char [], int , int , int , int , int );
    void delete_node(int);
    void delete_node(char []);
    void display();
    void Search();
    void modify();
    void billgen(char [], char [], int, int &);
    void SaveToFile();
    void ReadFromFile(LinkedList &);
    int recsnum()
    {
        FILE *fp;
        fp = fopen("product_store.txt","r");
        fseek(fp,0,2);
        int recs;
        recs = ftell(fp) / sizeof(s);
        fclose(fp);
        return recs;
    }
};

LinkedList::LinkedList()
{
    H = NULL;
}
LinkedList::~LinkedList()
{
    nodeptr T;
    while(H != NULL)
    {
        T = H;
        H = T->link;
        //cout << "Deleting node with data = " << T->pname << endl;
        delete T;
    }
}
int LinkedList::getcount()
{
    nodeptr T;
    T = H;
    int c = 0;
    while(T != NULL)
    {
        T = T->link;
        c++;
    }
    return c;
}
void LinkedList::add_front(char pname[], int pid, int price, int tquant, int aquant, int rack)
{
    if(H == NULL)
    {
        H = get_node();

        strcpy(H->pname,pname);
        H->pid = pid;
        H->price = price;
        H->tquant = tquant;
        H->aquant = aquant;
        H->rack = rack;

        H->link = NULL;
    }
    else
    {
        nodeptr N;
        N = get_node();

        strcpy(N->pname,pname);
        N->pid = pid;
        N->price = price;
        N->tquant = tquant;
        N->aquant = aquant;
        N->rack = rack;

        N->link = H;
        H = N;
    }

}
void LinkedList::add_end(char pname[], int pid, int price, int tquant, int aquant, int rack)
{
    if(H == NULL)
    {
        H = get_node();

        strcpy(H->pname,pname);
        H->pid = pid;
        H->price = price;
        H->tquant = tquant;
        H->aquant = aquant;
        H->rack = rack;

        H->link = NULL;
    }
    else
    {
        nodeptr T;
        T = H;
        while(T->link != NULL)  //Traverse to last node
            T = T->link;
        T->link = get_node();

        strcpy(T->link->pname,pname);
        T->link->pid = pid;
        T->link->price = price;
        T->link->tquant = tquant;
        T->link->aquant = aquant;
        T->link->rack = rack;

        T->link->link = NULL;
    }
}
void LinkedList::add_middle(int pos, char pname[], int pid, int price, int tquant, int aquant, int rack)
{
    nodeptr T,N;
    T = H;
    if(pos == 1)
        add_front(pname,pid,price,tquant,aquant,rack);
    else if(pos > getcount())
        cout << "Enter a valid position" << endl;
    else
    {
        for(int i = 1 ; i < pos - 1 ; i++)
        {
            T = T->link;
        }
        N = get_node();

        strcpy(N->pname,pname);
        N->pid = pid;
        N->price = price;
        N->tquant = tquant;
        N->aquant = aquant;
        N->rack = rack;

        N->link = T->link;
        T->link = N;
    }
}
void LinkedList::delete_node(int nodenum)
{
    nodeptr T,P;
    T = H;
    if(T == NULL);
    else if(T->link == NULL)    //Only one node
    {
        H = NULL;
        delete T;
    }
    else
    {
        if(nodenum > getcount())
            cout << "Enter a valid index" << endl;
        else
        {
            for(int i = 1 ; i < nodenum - 1 ; i++)
            {
                T = T->link;
            }
            P = T->link;
            T->link = P->link;
            delete P;
        }
    }
}
void LinkedList::delete_node(char name[])
{
    nodeptr T,P;
    T = H;
    P = T;
    if(T == nullptr);
    else if(stricmp(T->pname,name) == 0)
    {
        T = T ->link;
        H = T;
        delete P;
        P = T;
    }
    else
    {
        int flag = 0;
        for(int i = 1 ; i < getcount() ; i++)
        {
            if(stricmp(T->link->pname,name) == 0)
            {
                flag = 1;
                break;
            }
            T = T->link;
        }
        if(flag == 1)
        {
            P = T->link;
            T->link = T->link->link;
            delete P;
            cout << "Record deleted" << endl;
        }
        else
            cout << "Product not found" << endl;
    }
}
void LinkedList::display()
{
    system("CLS");
    nodeptr T;
    int cnt = 1;
    T = H;
    cout << "\n\nNumber of records = " << getcount() << endl;
    cout <<"\n\n";
    cout << setw(30) << "Product name" << "\t"
         << "pid" << "\t"
         << "Price" << "\t"
         << "Tquant" << "\t"
         << "Aquant" << "\t"
         << "Rack" << "\t"
         << "Address" << "\t\t"
         << "Link" << endl << endl;
    if(T == nullptr)
        cout << "List empty" << endl;
    while(T != nullptr)
    {
        cout << setw(30) << T->pname << "\t"
             << T->pid << "\t"
             << T->price << "\t"
             << T->tquant << "\t"
             << T->aquant << "\t"
             << T->rack << "\t"
             << T << "\t" << T->link << endl;

        cnt++;
        T = T->link;
    }
    cout<<"\n\n";
    system("PAUSE");
}

void LinkedList::modify()
{
    system("CLS");
    nodeptr T;
    char pname[30];
    cout << "Enter name of product whose record has to be modified : ";
    cin >> pname;
    int cnt = 1;
    int flag = 0;
    T = H;
    if(T == NULL)
        cout << "List empty" << endl;
    while(T != NULL)
    {
        if(stricmp(T->pname,pname) == 0)
        {
            cout << "----------------------------------------------------------------" << endl;
            cout << "Node number " << cnt << endl;
            cout << "----------------------------------------------------------------" << endl;
            cout << "Node address = " << T << endl;

            cout << "Product name : " << T->pname << endl
                 << "Product id : " << T->pid << endl
                 << "Price : " << T->price << endl
                 << "Total products initially : " << T->tquant << endl
                 << "Available products : " << T->aquant << endl
                 << "Rack number : " << T->rack << endl << endl;

            cout << "Re-enter data : ";
            cin >> T->pname >> T->pid >> T->price >> T->tquant >> T->aquant >> T->rack;

            flag = 1;
            break;
        }
        if(flag == 1)
            break;
        cnt++;
        T = T->link;

    }
}
void LinkedList::SaveToFile()
{
    FILE *fp;
    fp = fopen("product_store.txt","w");
    fclose(fp);
    nodeptr T;
    T = H;

    while(T != NULL)
    {
        strcpy(s.pname,T->pname);
        s.pid = T->pid;
        s.price = T->price;
        s.tquant = T->tquant;
        s.aquant = T->aquant;
        s.rack = T->rack;

        T = T->link;
        fp = fopen("product_store.txt","a");
        fwrite(&s,sizeof(s),1,fp);
        fclose(fp);
    }
}

void LinkedList::ReadFromFile(LinkedList &arg)
{
    FILE *fp;
    int recs = recsnum();
    fp = fopen("product_store.txt","r");
    for(int i = 1 ; i <= recs ; i++)
    {
        fread(&s,sizeof(s),1,fp);
        arg.add_end(s.pname,s.pid,s.price,s.tquant,s.aquant,s.rack);
    }
    fclose(fp);
}

void LinkedList::billgen(char filename[],char name[], int quantity, int &total)
{
    FILE *fp;
    fp = fopen(filename,"a");
    int flag = 0;
    nodeptr T;
    T = H;
    while(T != NULL)
    {
        if(stricmp(T->pname,name) == 0)
        {
            if(quantity > T->aquant)
                cout << "Requested number of products are not available" << endl;
            else
            {
                fprintf(fp,"%-30s\t%-6d\t%-6d\t\t%-6d\n",T->pname,quantity,T->price,quantity*T->price);
                T->aquant = T->aquant - quantity;
                total = total + quantity*T->price;
                flag = 1;
                break;
               fclose(fp);
            }
        }
        T = T->link;
        if(flag == 1)
            break;
    }
    if(flag == 0)
    {
        fclose(fp);
        cout << "Requested Product is not available" << endl;
    }
}

void LinkedList::Search()
{
    system("CLS");
    nodeptr T;
    char pname[30];

    cout << "\n\nEnter product name to be searched : ";
    cin >> pname;

    int flag = 0;
    T = H;
    if(T == nullptr)
        cout << "List empty" << endl;
    while(T != nullptr)
    {
        if(stricmp(T->pname,pname) == 0)
        {
            cout << "----------------------------------------------------------------" << endl;

            cout << "Product name : " << T->pname << endl
                 << "Product id : " << T->pid << endl
                 << "Price : " << T->price << endl
                 << "Total products initially : " << T->tquant << endl
                 << "Available products : " << T->aquant << endl
                 << "Rack number : " << T->rack << endl << endl;

            cout << "----------------------------------------------------------------" << endl;
            getch();
            flag = 1;
            break;
        }
        if(flag == 1)
            break;

        T = T->link;

    }
    if(flag == 0)
    {
        cout << "Product not found" << endl;
        getch();
    }
}

void filler();
void liner();
void welcome();
void exitscreen();

char pname[30]; //Product name
int pid;    //Product id
int price;    //Product price
int tquant; //Total products purchased from wholesale
int aquant; //How many are available in stock
int rack;

char filename[50];

class store
{
    LinkedList obj;
    int t;
public:
    store()
    {
        t = 0;
        obj.ReadFromFile(obj);
    }
    void add()
    {
        system("CLS");
        cout<<"\n\t\t\t[press enter after each details]";
        cout << "\nEnter Product name" << endl;
        cin >> pname;

        cout << "\nEnter Product id" << endl;
        cin >> pid;

        cout << "\nEnter Price" << endl;
        cin >> price;

        cout << "\nEnter Total Qty" << endl;
        cin >> tquant;

        cout << "\nEnter Available Qty" << endl;
        cin >> aquant;

        cout << "\nEnter Rack No" << endl;
        cin >> rack;
        
        obj.add_end(pname,pid,price,tquant,aquant,rack);
    }
    void display()
    {
        obj.display();
    }
    int getrecs()
    {
        return obj.recsnum();
    }
    void modify()
    {
        obj.modify();
    }
    void PrintBill();
    void deleteproduct()
    {
        system("CLS");
        char name[30];
        cout << "\n\nEnter name of product : ";
        cin >> name;
        obj.delete_node(name);
    }
    void SearchProduct()
    {
        obj.Search();
    }
    void totalprinter();
    ~store()
    {
        cout << "Number of records = " << obj.getcount() << endl;
        obj.SaveToFile();
       // exitscreen();
    }
};

void store::PrintBill()
{
    system("CLS");
    int choice;
    char sname[] = {"Product Name"};
    char name[30];
    int quantity;
    cout << "\n\nEnter filename for bill with full path and file extension : ";
    cin >> filename;
    FILE *fp;
    fp = fopen(filename,"a");
    for(int i = 0 ; i < 70 ; i++)
    {
        fprintf(fp,"*");
    }
    fprintf(fp,"\n");
    fprintf(fp,"%-30s\tQty.\tPrice/item\tAmount\n",sname);

    for(int i = 0 ; i < 70 ; i++)
    {
        fprintf(fp,"*");
    }
    fprintf(fp,"\n");
    fclose(fp);
    while(true)
    {
        cout << "\nContinue Purchasing Product ?\n1 = yes , 2 = no" << endl;
        cout << "choice : ";
        cin >> choice;
        if(choice == 1)
        {
            cout << "\nEnter product name and quantity : " << endl;
            cin >> name >> quantity;
            obj.billgen(filename,name,quantity,t);
        }
        else
            break;
    }
}

void store::totalprinter()
{
    FILE *fp;
    fp = fopen(filename,"a");
    fprintf(fp,"\n");
    for(int i = 0 ; i < 70 ; i++)
    {
        fprintf(fp,"*");
    }


    fprintf(fp,"\n");

    for(int i = 0 ; i < 70 ; i++)
    {
        fprintf(fp,"*");
    }
    fprintf(fp,"\n");
    fprintf(fp,"Total = %d\n",t);
    for(int i = 0 ; i < 70 ; i++)
    {
        fprintf(fp,"*");
    }
    fprintf(fp,"\n");
    fclose(fp);
}

int main()
{
    store obj;
    int ch;
    cout << endl << "Press any key to continue" << endl;
    getch();
    while(1)
    {
        system("CLS");
        cout <<"\n\n\t\t\t---------------------------------------------";
        cout << "\n\t\t\tSIMPLE ELECTRONIC STORE MANAGEMENT SYSTEM : \n\t\t\t---------------------------------------------" << endl
             << "\t\t\t\t (1) To Add Products" << endl
             << "\t\t\t\t (2) To Display Products" << endl
             << "\t\t\t\t (3) To Modify Products" << endl
             << "\t\t\t\t (4) To Delete Products" << endl
             << "\t\t\t\t (5) To Search Products" << endl
             << "\t\t\t\t (6) To Sell Products" << endl
             << "\t\t\t\t (7) Exit " << endl;
        cout << "\t\t\t Choice : ";
        cin >> ch;
        switch(ch)
        {
            case    1   :   obj.add();
                break;
            case    2   :   obj.display();
                getch();
                break;
            case    3   :   obj.modify();
                break;
            case    4   :   obj.deleteproduct();
                getch();
                break;
            case    5   :   obj.SearchProduct();
                break;
            case    6   :   obj.PrintBill();
                obj.totalprinter();
                getch();

                break;
            case    7   :   return 0;
        }
    }
}
