#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
typedef struct st_medicine{
    int medicine_id;
    char medicine_name[50];
    char company[50];
    char mfg[50];
    char exp[50];
    int quantity;
    float cost;
}st_medicine;
typedef struct st_customer{
    char birthdate[60];
    char firstname[40];
    char lastname[40];
    char address_line1[200];
    char address_line2[200];
    char city[20];
    char State[500];
    char province[50];
    char region[50];
    char country[40];
    int id_code;
}st_customer;
typedef struct st_supply {
    char supply_name[40];
    char company_name[40];
    int supply_id;
    char mfg[50];
    char exp[50];
    int quantity;
    float sale;
}st_supply;
typedef struct check_payment{
    float m_price;
    float m_quantity;
    float s_price;
    float s_quantity;
    float s_total_price;
    float total_price;
}check_payment;
typedef struct rate_us{
    int rate;
}rate_us;
void store_medicine(){
    int i, n_medicine;
    st_medicine *st;
    FILE *fp;
    printf("\n\t\t\tHow many types of medicines :");
    scanf("%d", &n_medicine);
    st = (st_medicine*)calloc(n_medicine, sizeof(st_medicine));
    fp = fopen("store_medicine.txt", "w");
    for (i = 0; i < n_medicine; i++) {
        st[i].medicine_id=0;
        st[i].cost=0;
        st[i].quantity=0;
        printf("\n\t\t\t%d. Medicine information\n", i + 1);
        printf("\n\t\t\tMEDICINE ID      :");
        scanf("%d", &st[i].medicine_id);
        fflush(stdin);
        printf("\t\t\tMEDICINE NAME    :");
        scanf("%s", st[i].medicine_name);
        printf("\t\t\tCOMPANY NAME     :");
        scanf("%s", st[i].company);
        printf("\t\t\tMFG DATE         :");
        scanf("%s", st[i].mfg);
        printf("\t\t\tEXP DATE         :");
        scanf("%s", st[i].exp);
        printf("\t\t\tQUANTITY         :");
        scanf("%d", &st[i].quantity);
        printf("\t\t\tSALE COST  ($)   :");
        scanf("%f", &st[i].cost);
        fwrite(&st[i], sizeof(st_medicine), 1, fp);
    }
    fclose(fp);
}
void check_medicine_info(){
    st_medicine st1;
    FILE *fp;
    fp = fopen("store_medicine.txt", "r");
    printf("\n------------------------------------------<< HERE IS ALL INFO OF MEDICINE >>--------------------------------------------");
    printf("\n\tMEDICINE ID\tMEDICINE NAME\tCOMPANY NAME\tMFG DATE\tEXP DATE\tQUANTITY\tSALE COST($)");
    printf("\n------------------------------------------------------------------------------------------------------------------------\n");
    while(fread(&st1, sizeof(st_medicine),1,fp)){
        printf("\n   -->   %d\t\t%s\t\t%s\t\t%s\t\t%s\t\t   %d\t\t  %.2f $\n", st1.medicine_id, st1.medicine_name, st1.company, st1.mfg, st1.exp, st1.quantity, st1.cost);
    }
    fclose(fp);
}
void update_medicine_info(){
    int rno, i;
    int found = 0;
    st_medicine st1;
    FILE *fp, *fp1;
    printf("\n\t\t\t\tTo update the information about medicine.\n");
    fp = fopen("store_medicine.txt", "r");
    fp1= fopen("store_temp_medicine.txt", "w");
    printf("\t\t\t\tPlease enter medicine's ID that exist :");
    scanf("%d", &rno);
    while(fread(&st1, sizeof(st_medicine), 1, fp)){
        if(st1.medicine_id==rno){
            found = 1;
            printf("\n\t\t\t-------------<< HERE IS MEDICINE INFO YOU WANT TO EDIT >>--------------\n");
            printf("\n\tMEDICINE ID\tMEDICINE NAME\tCOMPANY NAME\tMFG DATE\tEXP DATE\tQUANTITY\tSALE COST($)\n");
            printf("\n         %d\t\t%s\t\t%s\t\t%s\t\t%s\t\t   %d\t\t  %.2f $\n", st1.medicine_id, st1.medicine_name, st1.company, st1.mfg, st1.exp, st1.quantity, st1.cost);
            printf("\n\t\t\t\t\tWhich information that you want to edit ??\n");
            printf("\n\t\t\t\t\t1. EDIT ID");
            printf("\n\t\t\t\t\t2. EDIT Medicine Name");
            printf("\n\t\t\t\t\t3. EDIT Company Name");
            printf("\n\t\t\t\t\t4. EDIT MFG Date");
            printf("\n\t\t\t\t\t5. EDIT EXP Date");
            printf("\n\t\t\t\t\t6. EDIT Quantity");
            printf("\n\t\t\t\t\t7. EDIT Cost Price");
            printf("\n\n\t\t\t\t\tSelect your choice :");
            scanf("%d", &i);
            if(i==1){
                printf("\n\t\t\t\t\tENTER NEW MEDICINE ID      :");
                scanf("%d", &st1.medicine_id);
                fflush(stdin);
                printf("\n\t\t\t----------------------<< CHANGING SUCCESSFUL >>------------------------\n");
            }else if(i==2){
                printf("\n\t\t\t\t\tENTER NEW MEDICINE NAME    :");
                scanf("%s", st1.medicine_name);
                printf("\n\t\t\t----------------------<< CHANGING SUCCESSFUL >>------------------------\n");
            }else if(i==3){
                printf("\n\t\t\t\t\tENTER NEW COMPANY NAME     :");
                scanf("%s", st1.company);
                printf("\n\t\t\t----------------------<< CHANGING SUCCESSFUL >>------------------------\n");
            }else if(i==4){
                printf("\n\t\t\t\t\tENTER NEW MFG DATE         :");
                scanf("%s", st1.mfg);
                printf("\n\t\t\t----------------------<< CHANGING SUCCESSFUL >>------------------------\n");
            }else if(i==5){
                printf("\n\t\t\t\t\tENTER NEW EXP DATE         :");
                scanf("%s", st1.exp);
                printf("\n\t\t\t----------------------<< CHANGING SUCCESSFUL >>------------------------\n");
            }else if(i==6) {
                printf("\n\t\t\t\t\tENTER NEW QUANTITY         :");
                scanf("%d", &st1.quantity);
                printf("\n\t\t\t----------------------<< CHANGING SUCCESSFUL >>------------------------\n");
            }else if(i==7){
                printf("\n\t\t\t\t\tENTER NEW SALE COST  ($)   :");
                scanf("%f", &st1.cost);
                printf("\n\t\t\t----------------------<< CHANGING SUCCESSFUL >>------------------------\n");
            }else
                printf("\n\t\t\t\t\t\tWrong Choice!!!\n");
        }
        fwrite(&st1, sizeof(st_medicine), 1, fp1);
    }
    fclose(fp);
    fclose(fp1);
    if (found){
        fp1= fopen("store_temp_medicine.txt", "r");
        fp = fopen("store_medicine.txt", "w");
        while(fread(&st1, sizeof(st_medicine), 1, fp1)){
            fwrite(&st1, sizeof(st_medicine), 1, fp);
        }
        fclose(fp);
        fclose(fp1);
    }
    else
        printf("\n==============================================(( Information not found!!! ))============================================\n");
}
void append_store_medicine(){
    int i, n_medicine;
    st_medicine *st;
    FILE *fp;
    printf("\n\t\t\tHow many types of medicines :");
    scanf("%d", &n_medicine);
    st = (st_medicine*)calloc(n_medicine, sizeof(st_medicine));
    fp = fopen("store_medicine.txt", "a");
    for (i = 0; i < n_medicine; i++) {
        st[i].medicine_id=0;
        st[i].cost=0;
        st[i].quantity=0;
        printf("\n\t\t\t%d. Medicine information\n", i + 1);
        printf("\n\t\t\tMEDICINE ID      :");
        scanf("%d", &st[i].medicine_id);
        fflush(stdin);
        printf("\t\t\tMEDICINE NAME    :");
        scanf("%s", st[i].medicine_name);
        printf("\t\t\tCOMPANY NAME     :");
        scanf("%s", st[i].company);
        printf("\t\t\tMFG DATE         :");
        scanf("%s", st[i].mfg);
        printf("\t\t\tEXP DATE         :");
        scanf("%s", st[i].exp);
        printf("\t\t\tQUANTITY         :");
        scanf("%d", &st[i].quantity);
        printf("\t\t\tSALE COST  ($)   :");
        scanf("%f", &st[i].cost);
        fwrite(&st[i], sizeof(st_medicine), 1, fp);
    }
    fclose(fp);
}
void del_medicine_info(){
    int rno;
    int found = 0;
    st_medicine st1;
    FILE *fp, *fp1;
    printf("\n\t\t\t\tTo delete the information about medicine.\n");
    fp = fopen("store_medicine.txt", "r");
    fp1= fopen("store_temp_medicine.txt", "w");
    printf("\t\t\t\tPlease enter medicine's ID that exist :");
    scanf("%d", &rno);
    while(fread(&st1, sizeof(st_medicine), 1, fp)){
        if(st1.medicine_id==rno){
            found = 1;
        }
        else
            fwrite(&st1, sizeof(st_medicine), 1, fp1);
    }
    fclose(fp);
    fclose(fp1);
    if (found){
        fp1= fopen("store_temp_medicine.txt", "r");
        fp = fopen("store_medicine.txt", "w");
        while(fread(&st1, sizeof(st_medicine), 1, fp1)){
            fwrite(&st1, sizeof(st_medicine), 1, fp);
        }
        fclose(fp);
        fclose(fp1);
        printf("\n\t\t\t------------------------<< DELETE SUCCESSFUL >>------------------------\n");
    }
    else
        printf("\n==============================================(( Information not found!!! ))============================================\n");
}
void sort_medicine_info(){
    int i, j;
    st_medicine *st, st1;
    FILE *fp;
    fp = fopen("store_medicine.txt", "r");
    fseek(fp,0,SEEK_END);
    int n = ftell(fp)/sizeof(st_medicine);
    st = (st_medicine*)calloc(n, sizeof(st_medicine));
    rewind(fp);
    for (i=0; i<n; i++)
        fread(&st[i],sizeof(st_medicine),1,fp);
    fclose(fp);
    for (i=0; i<n; i++){
        for (j=i+1; j<n; j++){
            if (st[i].medicine_id > st[j].medicine_id ){
                st1 = st[i];
                st[i] = st[j];
                st[j] = st1;
            }
        }
    }
    fp = fopen("store_medicine.txt", "w");
    for (i=0; i<n; i++){
        fwrite(&st[i], sizeof(st_medicine), 1, fp);
    }
    fclose(fp);
}
void search_medicine_info(){
    int rno;
    int found = 0;
    st_medicine st1;
    FILE *fp;
    printf("\n\t\t\t\tTo find all information about medicine.\n");
    fp = fopen("store_medicine.txt", "r");
    printf("\t\t\t\tPlease enter medicine's ID :");
    scanf("%d", &rno);
    printf("\n------------------------------------<< HERE IS INFO OF MEDICINE YOU WANT TO FIND >>-------------------------------------");
    printf("\n\tMEDICINE ID\tMEDICINE NAME\tCOMPANY NAME\tMFG DATE\tEXP DATE\tQUANTITY\tSALE COST($)");
    printf("\n------------------------------------------------------------------------------------------------------------------------\n");
    while(fread(&st1, sizeof(st_medicine), 1, fp)){
        if(st1.medicine_id==rno){
            found = 1;
            printf("\n   ==>   %d\t\t%s\t\t%s\t\t%s\t\t%s\t\t   %d\t\t  %.2f $\n", st1.medicine_id, st1.medicine_name, st1.company, st1.mfg, st1.exp, st1.quantity, st1.cost);
        }
    }
    if (!found)
        printf("\n==============================================(( Information not found!!! ))============================================\n");
    fclose(fp);
}
void store_customer_info(){
    int n, i;
    st_customer *stc;
    FILE *fp;
    printf("\n\t\t\tHow many customer :");
    scanf("%d", &n);
    stc = (st_customer *)calloc(n, sizeof(st_customer));
    fp = fopen("store_customer.txt", "w");
    for (i = 0; i < n; i++) {
        printf("\n\t\t\t%d. Customer information\n", i + 1);
        printf("\n\t\t\tIdentify Code         :");
        scanf("%d", &stc[i].id_code);
        fflush(stdin);
        printf("\t\t\tFirst name            :");
        scanf("%s", stc[i].firstname);
        printf("\t\t\tLast name             :");
        scanf("%s", stc[i].lastname);
        printf("\t\t\tBirth Date(dd/mm/yyyy):");
        scanf("%s", stc[i].birthdate);
        printf("\t\t\tAddress Line 1        :");
        scanf("%s", stc[i].address_line1);
        printf("\t\t\tAddress Line 2        :");
        scanf("%s", stc[i].address_line2);
        printf("\t\t\tCity                  :");
        scanf("%s", stc[i].city);
        printf("\t\t\tState                 :");
        scanf("%s", stc[i].State);
        printf("\t\t\tProvince              :");
        scanf("%s", stc[i].province);
        printf("\t\t\tRegion                :");
        scanf("%s", stc[i].region);
        printf("\t\t\tCountry               :");
        scanf("%s", stc[i].country);
        fwrite(&stc[i], sizeof(st_customer), 1, fp);
    }
    fclose(fp);
}
void check_customer_info(){
    st_customer stc1;
    FILE *fp;
    fp = fopen("store_customer.txt", "r");
    printf("\n------------------------------------------<< HERE IS ALL INFO OF CUSTOMER >>--------------------------------------------");
    printf("\n\tCUSTOMER ID\tFIRST NAME\tLAST NAME\tBIRTH DATE\tCITY\t\tSTATE\t\tPROVINCE");
    printf("\n------------------------------------------------------------------------------------------------------------------------\n");
    while(fread(&stc1, sizeof(st_customer),1,fp)){
        printf("\n   -->   %d\t\t%s\t\t%s\t\t%s\t\t%s\t\t%s\t\t%s\n",stc1.id_code, stc1.firstname, stc1.lastname, stc1.birthdate, stc1.city, stc1.State, stc1.province);
    }
    fclose(fp);
}
void update_customer_info(){
    int id_customer;
    int found = 0;
    st_customer stc1;
    FILE *fp, *fp1;
    printf("\n\t\t\t\tTo update the information about customer.\n");
    fp = fopen("store_customer.txt", "r");
    fp1 = fopen("store_temp_customer.txt", "w");
    printf("\t\t\t\tPlease enter customer's ID that exist :");
    scanf("%d", &id_customer);
    while(fread(&stc1, sizeof(st_customer),1,fp)){
        if(stc1.id_code==id_customer){
            found = 1;
            printf("\n\t\t\t\tEnter new Identify Code         :");
            scanf("%d", &stc1.id_code);
            fflush(stdin);
            printf("\t\t\t\tEnter new First name            :");
            scanf("%s", stc1.firstname);
            printf("\t\t\t\tEnter new Last name             :");
            scanf("%s", stc1.lastname);
            printf("\t\t\t\tEnter new Birth Date(dd/mm/yyyy):");
            scanf("%s", stc1.birthdate);
            printf("\t\t\t\tEnter new Address Line 1        :");
            scanf("%s", stc1.address_line1);
            printf("\t\t\t\tEnter new Address Line 2        :");
            scanf("%s", stc1.address_line2);
            printf("\t\t\t\tEnter new City                  :");
            scanf("%s", stc1.city);
            printf("\t\t\t\tEnter new State                 :");
            scanf("%s", stc1.State);
            printf("\t\t\t\tEnter new Province              :");
            scanf("%s", stc1.province);
            printf("\t\t\t\tEnter new Region                :");
            scanf("%s", stc1.region);
            printf("\t\t\t\tEnter new Country               :");
            scanf("%s", stc1.country);
        }
        fwrite(&stc1, sizeof(st_customer), 1, fp1);
    }
    fclose(fp);
    fclose(fp1);
    if (found){
        fp1 = fopen("store_temp_customer.txt", "r");
        fp = fopen("store_customer.txt", "w");
        while(fread(&stc1, sizeof(st_customer),1,fp1)){
            fwrite(&stc1, sizeof(st_customer), 1, fp);
        }
        fclose(fp);
        fclose(fp1);
    }
    else
        printf("\n==============================================(( Information not found!!! ))============================================\n");
}
void append_store_customer_info(){
    int n, i;
    st_customer *stc;
    FILE *fp;
    printf("\n\t\t\tHow many customer :");
    scanf("%d", &n);
    stc = (st_customer *)calloc(n, sizeof(st_customer));
    fp = fopen("store_customer.txt", "a");
    for (i = 0; i < n; i++) {
        printf("\n\t\t\t%d. Customer information\n", i + 1);
        printf("\n\t\t\tIdentify Code         :");
        scanf("%d", &stc[i].id_code);
        fflush(stdin);
        printf("\t\t\tFirst name            :");
        scanf("%s", stc[i].firstname);
        printf("\t\t\tLast name             :");
        scanf("%s", stc[i].lastname);
        printf("\t\t\tBirth Date(dd/mm/yyyy):");
        scanf("%s", stc[i].birthdate);
        printf("\t\t\tAddress Line 1        :");
        scanf("%s", stc[i].address_line1);
        printf("\t\t\tAddress Line 2        :");
        scanf("%s", stc[i].address_line2);
        printf("\t\t\tCity                  :");
        scanf("%s", stc[i].city);
        printf("\t\t\tState                 :");
        scanf("%s", stc[i].State);
        printf("\t\t\tProvince              :");
        scanf("%s", stc[i].province);
        printf("\t\t\tRegion                :");
        scanf("%s", stc[i].region);
        printf("\t\t\tCountry               :");
        scanf("%s", stc[i].country);
        fwrite(&stc[i], sizeof(st_customer), 1, fp);
    }
    fclose(fp);
}
void del_customer_info(){
    int id_customer;
    int found = 0;
    st_customer stc1;
    FILE *fp, *fp1;
    printf("\n\t\t\t\tTo delete the information about customer.\n");
    fp = fopen("store_customer.txt", "r");
    fp1 = fopen("store_temp_customer.txt", "w");
    printf("\t\t\t\tPlease enter customer's ID that exist :");
    scanf("%d", &id_customer);
    while(fread(&stc1, sizeof(st_customer),1,fp)){
        if(stc1.id_code==id_customer){
            found = 1;
        }
        else
            fwrite(&stc1, sizeof(st_customer), 1, fp1);
    }
    fclose(fp);
    fclose(fp1);
    if (found){
        fp1 = fopen("store_temp_customer.txt", "r");
        fp = fopen("store_customer.txt", "w");
        while(fread(&stc1, sizeof(st_customer),1,fp1)){
            fwrite(&stc1, sizeof(st_customer), 1, fp);
        }
        fclose(fp);
        fclose(fp1);
        printf("\n\t\t\t------------------------<< DELETE SUCCESSFUL >>------------------------\n");
    }
    else
        printf("\n==============================================(( Information not found!!! ))============================================\n");
}
void sort_customer_info(){
    int i, j;
    st_customer *stc, stc1;
    FILE *fp;
    fp = fopen("store_customer.txt", "r");
    fseek(fp,0,SEEK_END);
    int n = ftell(fp)/sizeof(st_customer);
    stc = (st_customer*)calloc(n, sizeof(st_customer));
    rewind(fp);
    for (i=0; i<n; i++)
        fread(&stc[i], sizeof(st_customer),1,fp);
    fclose(fp);
    for (i=0; i<n; i++){
        for (j=i+1; j<n; j++){
            if (stc[i].id_code > stc[j].id_code){
                stc1 = stc[i];
                stc[i] = stc[j];
                stc[j] = stc1;
            }
        }
    }
    fp = fopen("store_customer.txt", "w");
    for (i=0; i<n; i++){
        fwrite(&stc[i], sizeof(st_customer),1,fp);
    }
    fclose(fp);
}
void search_customer_info(){
    int id_customer;
    int found = 0;
    st_customer stc1;
    FILE *fp;
    printf("\n\t\t\t\tTo find all information about customer.\n");
    fp = fopen("store_customer.txt", "r");
    printf("\t\t\t\tPlease enter customer's ID :");
    scanf("%d", &id_customer);
    printf("\n\t\t\t--------------<< HERE IS CLEAR INFO YOU WANT TO FIND >>----------------\n");
    while(fread(&stc1, sizeof(st_customer),1,fp)){
        if(stc1.id_code==id_customer){
            found = 1;
            printf("\n\t\t\t\tIdentify Code         : %d", stc1.id_code);
            printf("\n\t\t\t\tFirst name            : %s", stc1.firstname);
            printf("\n\t\t\t\tLast name             : %s", stc1.lastname);
            printf("\n\t\t\t\tBirth Date(dd/mm/yyyy): %s", stc1.birthdate);
            printf("\n\t\t\t\tAddress Line 1        : %s", stc1.address_line1);
            printf("\n\t\t\t\tAddress Line 2        : %s", stc1.address_line2);
            printf("\n\t\t\t\tCity                  : %s", stc1.city);
            printf("\n\t\t\t\tState                 : %s", stc1.State);
            printf("\n\t\t\t\tProvince              : %s", stc1.province);
            printf("\n\t\t\t\tRegion                : %s", stc1.region);
            printf("\n\t\t\t\tCountry               : %s\n", stc1.country);
        }
    }
    if (!found)
        printf("\n==============================================(( Information not found!!! ))============================================\n");
    fclose(fp);
}
void store_supplies(){
    int i, n_supply;
    st_supply *sts;
    FILE *fp;
    printf("\n\t\t\tHow many type of supply :");
    scanf("%d", &n_supply);
    sts = (st_supply *)calloc(n_supply, sizeof(st_supply));
    fp = fopen("store_supplies.txt", "w");
    for (i=0; i<n_supply; i++){
        printf("\n\t\t\t%d. Supply information\n", i+1);
        printf("\n\t\t\tSUPPLY ID        :");
        scanf("%d", &sts[i].supply_id);
        printf("\t\t\tSUPPLY NAME      :");
        scanf("%s", sts[i].supply_name);
        printf("\t\t\tCOMPANY NAME     :");
        scanf("%s", sts[i].company_name);
        printf("\t\t\tMFG DATE         :");
        scanf("%s", sts[i].mfg);
        printf("\t\t\tEXP DATE         :");
        scanf("%s", sts[i].exp);
        printf("\t\t\tQUANTITY         :");
        scanf("%d", &sts[i].quantity);
        printf("\t\t\tSALE COST  ($)   :");
        scanf("%f", &sts[i].sale);
        fwrite(&sts[i], sizeof(st_supply), 1, fp);
    }
    fclose(fp);
}
void check_supplies_info(){
    st_supply sts1;
    FILE *fp;
    fp = fopen("store_supplies.txt", "r");
    printf("\n------------------------------------------<< HERE IS ALL INFO OF SUPPLIES >>--------------------------------------------");
    printf("\n\tSUPPLY ID\tSUPPLY NAME\tCOMPANY NAME\tMFG DATE\tEXP DATE\tQUANTITY\tSALE COST($)");
    printf("\n------------------------------------------------------------------------------------------------------------------------\n");
    while(fread(&sts1, sizeof(st_supply),1,fp)){
        printf("\n   -->   %d\t\t%s\t\t%s\t\t%s\t\t%s\t\t   %d\t\t  %.2f $\n", sts1.supply_id, sts1.supply_name, sts1.company_name, sts1.mfg, sts1.exp, sts1.quantity, sts1.sale);
    }
    fclose(fp);
}
void update_supply_info(){
    int id_supply, i;
    int found = 0;
    st_supply sts1;
    FILE *fp, *fp1;
    printf("\n\t\t\t\tTo update the information about supplies.\n");
    fp = fopen("store_supplies.txt", "r");
    fp1 = fopen("store_temp_supplies.txt", "w");
    printf("\t\t\t\tPlease enter supply's ID that exist :");
    scanf("%d", &id_supply);
    while(fread(&sts1, sizeof(st_supply),1,fp)){
        if(sts1.supply_id==id_supply){
            found = 1;
            printf("\n\t\t\t--------------<< HERE IS SUPPLY INFO YOU WANT TO EDIT >>---------------\n");
            printf("\n\tSUPPLY ID\tSUPPLY NAME\tCOMPANY NAME\tMFG DATE\tEXP DATE\tQUANTITY\tSALE COST($)\n");
            printf("\n         %d\t\t%s\t\t%s\t\t%s\t\t%s\t\t   %d\t\t  %.2f $\n", sts1.supply_id, sts1.supply_name, sts1.company_name, sts1.mfg, sts1.exp, sts1.quantity, sts1.sale);
            printf("\n\t\t\t\t\tWhich information that you want to edit ??\n");
            printf("\n\t\t\t\t\t1. EDIT ID");
            printf("\n\t\t\t\t\t2. EDIT Supply Name");
            printf("\n\t\t\t\t\t3. EDIT Company Name");
            printf("\n\t\t\t\t\t4. EDIT MFG Date");
            printf("\n\t\t\t\t\t5. EDIT EXP Date");
            printf("\n\t\t\t\t\t6. EDIT Quantity");
            printf("\n\t\t\t\t\t7. EDIT Cost Price");
            printf("\n\n\t\t\t\t\tSelect your choice :");
            scanf("%d", &i);
            if(i==1){
                printf("\n\t\t\t\t\tENTER NEW SUPPLY ID        :");
                scanf("%d", &sts1.supply_id);
                fflush(stdin);
                printf("\n\t\t\t----------------------<< CHANGING SUCCESSFUL >>------------------------\n");
            }else if(i==2){
                printf("\n\t\t\t\t\tENTER NEW SUPPLY NAME      :");
                scanf("%s", sts1.supply_name);
                printf("\n\t\t\t----------------------<< CHANGING SUCCESSFUL >>------------------------\n");
            }else if(i==3){
                printf("\n\t\t\t\t\tENTER NEW COMPANY NAME     :");
                scanf("%s", sts1.company_name);
                printf("\n\t\t\t----------------------<< CHANGING SUCCESSFUL >>------------------------\n");
            }else if(i==4){
                printf("\n\t\t\t\t\tENTER NEW MFG DATE         :");
                scanf("%s", sts1.mfg);
                printf("\n\t\t\t----------------------<< CHANGING SUCCESSFUL >>------------------------\n");
            }else if(i==5){
                printf("\n\t\t\t\t\tENTER NEW EXP DATE         :");
                scanf("%s", sts1.exp);
                printf("\n\t\t\t----------------------<< CHANGING SUCCESSFUL >>------------------------\n");
            }else if(i==6) {
                printf("\n\t\t\t\t\tENTER NEW QUANTITY         :");
                scanf("%d", &sts1.quantity);
                printf("\n\t\t\t----------------------<< CHANGING SUCCESSFUL >>------------------------\n");
            }else if(i==7){
                printf("\n\t\t\t\t\tENTER NEW SALE COST  ($)   :");
                scanf("%f", &sts1.sale);
                printf("\n\t\t\t----------------------<< CHANGING SUCCESSFUL >>------------------------\n");
            }else
                printf("\n\t\t\t\t\t\tWrong Choice!!!\n");
        }
        fwrite(&sts1, sizeof(st_supply), 1, fp1);
    }
    fclose(fp);
    fclose(fp1);
    if(found){
        fp1 = fopen("store_temp_supplies.txt", "r");
        fp = fopen("store_supplies.txt", "w");
        while(fread(&sts1, sizeof(st_supply),1,fp1)){
            fwrite(&sts1, sizeof(st_supply), 1, fp);
        }
        fclose(fp);
        fclose(fp1);
    }
    else
        printf("\n==============================================(( Information not found!!! ))============================================\n");
}
void append_store_supplies(){
    int k, n_supply;
    st_supply *sts;
    FILE *fp;
    printf("\n\t\t\tHow many type of supply :");
    scanf("%d", &n_supply);
    sts = (st_supply *)calloc(n_supply, sizeof(st_supply));
    fp = fopen("store_supplies.txt", "a");
    for (k=0; k<n_supply; k++){
        printf("\n\t\t\t%d. Supply information\n", k+1);
        printf("\n\t\t\tSUPPLY ID        :");
        scanf("%d", &sts[k].supply_id);
        printf("\t\t\tSUPPLY NAME      :");
        scanf("%s", sts[k].supply_name);
        printf("\t\t\tCOMPANY NAME     :");
        scanf("%s", sts[k].company_name);
        printf("\t\t\tMFG DATE         :");
        scanf("%s", sts[k].mfg);
        printf("\t\t\tEXP DATE         :");
        scanf("%s", sts[k].exp);
        printf("\t\t\tQUANTITY         :");
        scanf("%d", &sts[k].quantity);
        printf("\t\t\tSALE COST  ($)   :");
        scanf("%f", &sts[k].sale);
        fwrite(&sts[k], sizeof(st_supply), 1, fp);
    }
    fclose(fp);
}
void del_supply_info(){
    int id_supply;
    int found = 0;
    st_supply sts1;
    FILE *fp, *fp1;
    printf("\n\t\t\t\tTo delete the information about supplies.\n");
    fp = fopen("store_supplies.txt", "r");
    fp1 = fopen("store_temp_supplies.txt", "w");
    printf("\t\t\t\tPlease enter supply's ID that exist :");
    scanf("%d", &id_supply);
    while(fread(&sts1, sizeof(st_supply),1,fp)){
        if(sts1.supply_id==id_supply){
            found = 1;
        }
        else
            fwrite(&sts1, sizeof(st_supply), 1, fp1);
    }
    fclose(fp);
    fclose(fp1);
    if(found){
        fp1 = fopen("store_temp_supplies.txt", "r");
        fp = fopen("store_supplies.txt", "w");
        while(fread(&sts1, sizeof(st_supply),1,fp1)){
            fwrite(&sts1, sizeof(st_supply), 1, fp);
        }
        fclose(fp);
        fclose(fp1);
        printf("\n\t\t\t------------------------<< DELETE SUCCESSFUL >>------------------------\n");
    }
    else
        printf("\n==============================================(( Information not found!!! ))============================================\n");
}
void sort_supply_info(){
    int i, j;
    st_supply *sts, sts1;
    FILE *fp;
    fp = fopen("store_supplies.txt", "r");
    fseek(fp,0,SEEK_END);
    int n = ftell(fp)/sizeof(st_supply);
    sts = (st_supply*)calloc(n, sizeof(st_supply));
    rewind(fp);
    for (i=0; i<n; i++)
        fread(&sts[i], sizeof(st_supply), 1, fp);
    fclose(fp);
    for (i=0; i<n; i++){
        for(j=i+1; j<n; j++){
            if (sts[i].supply_id > sts[j].supply_id){
                sts1 = sts[i];
                sts[i] = sts[j];
                sts[j] = sts1;
            }
        }
    }
    fp = fopen("store_supplies.txt", "w");
    for (i=0; i<n; i++){
        fwrite(&sts[i], sizeof(st_supply),1,fp);
    }
    fclose(fp);
}
void search_supplies_info(){
    int id_supply;
    int found = 0;
    st_supply sts1;
    FILE *fp;
    printf("\n\t\t\t\tTo find all information about supplies.\n");
    fp = fopen("store_supplies.txt", "r");
    printf("\t\t\t\tPlease enter supply's ID :");
    scanf("%d", &id_supply);
    printf("\n-------------------------------------<< HERE IS INFO OF SUPPLY YOU WANT TO FIND >>--------------------------------------");
    printf("\n\tSUPPLY ID\tSUPPLY NAME\tCOMPANY NAME\tMFG DATE\tEXP DATE\tQUANTITY\tSALE COST($)");
    printf("\n------------------------------------------------------------------------------------------------------------------------\n");
    while(fread(&sts1, sizeof(st_supply),1,fp)){
        if(sts1.supply_id==id_supply){
            found = 1;

            printf("\n   ==>   %d\t\t%s\t\t%s\t\t%s\t\t%s\t\t   %d\t\t  %.2f $\n", sts1.supply_id, sts1.supply_name, sts1.company_name, sts1.mfg, sts1.exp, sts1.quantity, sts1.sale);
        }
    }
    if (!found)
        printf("\n==============================================(( Information not found!!! ))============================================\n");
    fclose(fp);
}
void customer_payment(){
    int i, b, pay_m, pay_s;
    float m_total, s_total, total;
    check_payment *p;
    FILE *fp, *fp1;
    printf("\t\t\t\tTo check payment!!!\n");
    printf("\t\t\t\tPlease enter information about what you bought below :\n");
    printf("\n\t\t\t\tHow many type of medicines you bought :");
    scanf("%d", &pay_m);
    printf("\t\t\t\tHow many type of supplies you bought  :");
    scanf("%d", &pay_s);
    for (i=0; i<1; i++){
        p = (check_payment*)calloc(pay_m, sizeof(check_payment));
        fp = fopen("payment_info.txt", "w");
        for (b=0; b<pay_m; b++){
            printf("\n\t\t\t\t<< MEDICINE TYPE %d >>\n", b+1);
            printf("\t\t\t\tEnter price          :");
            scanf("%f", &p[b].m_price);
            printf("\t\t\t\tEnter quantity       :");
            scanf("%f", &p[b].m_quantity);
            p[b].total_price=(p[b].m_quantity*p[b].m_price);
            printf("\t\t\t\tType %d total price : %.2f $\n", b+1, p[b].total_price);
            m_total = m_total + p[b].total_price;
            fwrite(&p[b], sizeof(check_payment), 1, fp);
        }
        fclose(fp);
        p = (check_payment*)calloc(pay_s, sizeof(check_payment));
        fp1 = fopen("payment_s_info.txt", "a");
        for (b=0; b<pay_s; b++){
            printf("\n\t\t\t\t<< SUPPLY TYPE %d   >>\n", b+1);
            printf("\t\t\t\tEnter price          :");
            scanf("%f", &p[b].s_price);
            printf("\t\t\t\tEnter quantity       :");
            scanf("%f", &p[b].s_quantity);
            p[b].s_total_price=(p[b].s_quantity*p[b].s_price);
            printf("\t\t\t\tType %d total price : %.2f $\n", b+1, p[b].s_total_price);
            s_total = s_total + p[b].s_total_price;
            fwrite(&p[b], sizeof(check_payment), 1, fp1);
        }
        fclose(fp1);
    }
    total = m_total + s_total;
    printf("\n\t\t\t\tTOTAL PRICE OF ALL YOU BOUGHT IS %.2f $\n", total);
}
void rate(){
    const int r=1;
    rate_us rt;
    printf("\n\t\t\t\t\t\tHOW ABOUT OUR SERVICES ?\n");
    printf("\n\t\t\t\t\t\t1. Bad\t2. Good\t3. Best");
    printf("\n\n\t\t\t\t\t\t\tSelect :");
    scanf("%d", &rt.rate);
    if(rt.rate==1){
        FILE *fp;
        fp = fopen("rate_bad.txt", "a");
        fprintf(fp, "bad");
        fclose(fp);
    }else if(rt.rate==2){
        FILE *fp;
        fp = fopen("rate_good.txt", "a");
        fprintf(fp, "good");
        fclose(fp);
    }else if(rt.rate==3){
        FILE *fp;
        fp = fopen("rate_best.txt", "a");
        fprintf(fp, "best");
        fclose(fp);
    }
    printf("\n\t\t\t\t\t      FOR SERVICES OUR REVIEW IS :\n");
    FILE *fp1, *fp2, *fp3;
    fp1 = fopen("rate_bad.txt", "r");
    fseek(fp1, 0, SEEK_END);
    int n = ftell(fp1)/sizeof(rate_us);
    printf("\n\t\t\t\t\t\t---> BAD  is %d records\n", n);
    fclose(fp1);
    fp2 = fopen("rate_good.txt", "r");
    fseek(fp2, 0, SEEK_END);
    int m = ftell(fp2)/sizeof(rate_us);
    printf("\n\t\t\t\t\t\t---> GOOD is %d records\n", m);
    fclose(fp2);
    fp3 = fopen("rate_best.txt", "r");
    fseek(fp3, 0, SEEK_END);
    int o = ftell(fp3)/sizeof(rate_us);
    printf("\n\t\t\t\t\t\t---> BEST is %d records\n", o);
    fclose(fp3);
    printf("\n\t\t\t\t\t\t      THANK YOU !!\n");
}
int main(){
    int ch, i, j, k, l, b, c;
    char chc, cha;
    char choice;
    do{
        system("cls");
        system("COLOR 0A");
        printf("\n-------------------------------------------------<< THE--FALCON TEAM >>-------------------------------------------------");
        printf("\n\t\t\t\t\t <<<< WELCOME TO OUR MEDICAL STORE >>>>\n");
        printf("-------------------------------------------------<< HERE IS THE MENU >>-------------------------------------------------");
        printf("\n\t\t\t1. Add Medicine's Info");
        printf("\n\t\t\t2. Add Customer's Info");
        printf("\n\t\t\t3. Add Supply's Info");
        printf("\n\t\t\t4. Check Medicine's Info");
        printf("\n\t\t\t5. Check Customer's Info");
        printf("\n\t\t\t6. Check Supply's Info");
        printf("\n\t\t\t7. Check Customer Payment");
        printf("\n\t\t\t8. RATE US !!");
        printf("\n\t\t\t9. EXIT !!");
        printf("\n------------------------------------------------------------------------------------------------------------------------");
        printf("\n\t\t\tSelect Your Choice :");
        scanf("%d", &ch);
        switch (ch) {
            case 1:
                do{
                    system("cls");
                    system("COLOR 09");
                    printf("\n\n");
                    printf("\n\t\t\t-------------------<< WELCOME TO ADD MEDICINE MENU >>-------------------\n");
                    printf("\n\t\t\t1. To Create first Info List and Add First Info");
                    printf("\n\t\t\t2. To Add Medicine's Info");
                    printf("\n\t\t\t3. To Reset List and Create new List");
                    printf("\n\t\t\t4. Back to main menu\n");
                    printf("\n\t\t\t(*NOTE*)   | When First Info list created! No need to create again !! ");
                    printf("\n\t\t\t           | Just go << 2. To Add Medicine's Info >> !!\n");
                    printf("\n\t\t\tSelect your choice :");
                    scanf("%d", &l);
                    if(l == 1){
                        printf("\n\t\t\t-------------------<< Fill the medicine info below >>------------------");
                        store_medicine();
                        printf("\n\t\t\t-----------------<< Information is completely stored >>----------------\n");
                    }
                    else if(l == 2){
                        do{
                            printf("\n\t\t\t-------------------<< Fill the medicine info below >>------------------");
                            append_store_medicine();
                            printf("\n\t\t\t\tPress 'y' to add more info. Press 'n' for back to main menu.");
                            chc = getche();
                            printf("\n");
                        }while(chc=='y');
                        printf("\n\t\t\t-----------------<< Information is completely stored >>----------------\n");
                    }
                    else if(l == 3){
                        printf("\n\t\t\t\tOld List was reset!! Please enter new Info to store!!!\n");
                        printf("\n\t\t\t-------------------<< Fill the medicine info below >>------------------");
                        store_medicine();
                        printf("\n\t\t\t-----------------<< Information is completely stored >>----------------\n");
                    }
                    else if(l == 4){

                    }
                    else {
                        printf("\n\t\t\t\tWrong Choice!!!\n");
                    }
                    printf("\n\t\t\t   Press 'y' to select other choice. Press 'n' for back to main menu.");
                    cha = getche();
                    printf("\n");
                }while(cha=='y');
                break;
            case 2:
                do{
                    system("cls");
                    system("COLOR 09");
                    printf("\n\n");
                    printf("\n\t\t\t-------------------<< WELCOME TO ADD CUSTOMER MENU >>-------------------\n");
                    printf("\n\t\t\t1. To Create first Info List and Add First Info");
                    printf("\n\t\t\t2. To Add Customer's Info");
                    printf("\n\t\t\t3. To Reset List and Create new List");
                    printf("\n\t\t\t4. Back to main menu\n");
                    printf("\n\t\t\t(*NOTE*)   | When First Info list created! No need to create again !! ");
                    printf("\n\t\t\t           | Just go << 2. To Add Customer's Info >> !!\n");
                    printf("\n\t\t\tSelect your choice :");
                    scanf("%d", &b);
                    if(b==1){
                        printf("\n\t\t\t-------------------<< Fill the customer info below >>------------------");
                        store_customer_info();
                        printf("\n\t\t\t-----------------<< Information is completely stored >>----------------\n");
                    }
                    else if(b==2){
                        do{
                            printf("\n\t\t\t-------------------<< Fill the customer info below >>------------------");
                            append_store_customer_info();
                            printf("\n\t\t\t\tPress 'y' to add more info. Press 'n' for back to main menu.");
                            chc = getche();
                            printf("\n");
                        }while(chc=='y');
                        printf("\n\t\t\t-----------------<< Information is completely stored >>----------------\n");
                    }
                    else if(b==3){
                        printf("\n\t\t\t\tOld List was reset!! Please enter new Info to store!!!\n");
                        printf("\n\t\t\t-------------------<< Fill the customer info below >>------------------");
                        store_customer_info();
                        printf("\n\t\t\t-----------------<< Information is completely stored >>----------------\n");
                    }
                    else if(b==4){

                    }
                    else {
                        printf("\n\t\t\t\tWrong Choice!!!\n");
                    }
                    printf("\n\t\t\t   Press 'y' to select other choice. Press 'n' for back to main menu.");
                    cha = getche();
                    printf("\n");
                }while(cha=='y');
                break;
            case 3:
                do{
                    system("cls");
                    system("COLOR 09");
                    printf("\n\n");
                    printf("\n\t\t\t--------------------<< WELCOME TO ADD SUPPLY MENU >>--------------------\n");
                    printf("\n\t\t\t1. To Create first Info List and Add First Info");
                    printf("\n\t\t\t2. To Add Supply's Info");
                    printf("\n\t\t\t3. To Reset List and Create new List");
                    printf("\n\t\t\t4. Back to main menu\n");
                    printf("\n\t\t\t(*NOTE*)   | When First Info list created! No need to create again !! ");
                    printf("\n\t\t\t           | Just go << 2. To Add Supply's Info >> !!\n");
                    printf("\n\t\t\tSelect your choice :");
                    scanf("%d", &c);
                    if(c==1){
                        printf("\n\t\t\t-------------------<< Fill the supplies info below >>------------------");
                        store_supplies();
                        printf("\n\t\t\t-----------------<< Information is completely stored >>----------------\n");
                    }
                    else if(c==2){
                        do{
                            printf("\n\t\t\t-------------------<< Fill the supplies info below >>------------------");
                            append_store_supplies();
                            printf("\n\t\t\t\tPress 'y' to add more info. Press 'n' for back to main menu.");
                            chc = getche();
                            printf("\n");
                        }while(chc=='y');
                        printf("\n\t\t\t-----------------<< Information is completely stored >>----------------\n");
                    }
                    else if(c==3){
                        printf("\n\t\t\t\tOld List was reset!! Please enter new Info to store!!!\n");
                        printf("\n\t\t\t-------------------<< Fill the supplies info below >>------------------");
                        store_supplies();
                        printf("\n\t\t\t-----------------<< Information is completely stored >>----------------\n");
                    }
                    else if(c==4){

                    }
                    else {
                        printf("\n\t\t\t\tWrong Choice!!!\n");
                    }
                    printf("\n\t\t\t   Press 'y' to select other choice. Press 'n' for back to main menu.");
                    cha = getche();
                    printf("\n");
                }while(cha=='y');
                break;
            case 4:
                do{
                    system("cls");
                    system("COLOR 09");
                    printf("\n\n");
                    printf("\n\t\t\t--------------<< WELCOME TO CHECK MEDICINE'S INFO MENU >>--------------\n\n");
                    printf("\t\t\t\t--------------------\n");
                    printf("\t\t\t\t1. To Search Info by ID\n");
                    printf("\t\t\t\t2. To Display All Info\n");
                    printf("\t\t\t\t3. To Edit Info by ID\n");
                    printf("\t\t\t\t4. To Sort Info by ID\n");
                    printf("\t\t\t\t5. To Delete Info by ID\n");
                    printf("\t\t\t\t6. To Back to main menu\n");
                    printf("\t\t\t\t--------------------\n");
                    printf("\t\t\t\tSelect your choice :");
                    scanf("%d", &i);
                    if(i==1){
                        search_medicine_info();
                    }
                    else if(i==2){
                        check_medicine_info();
                    }
                    else if(i==3){
                        update_medicine_info();
                    }
                    else if(i==4){
                        printf("\n");
                        sort_medicine_info();
                        printf("\n\t\t\t---------------------<< SORT LIST SUCCESSFUL >>------------------------\n");
                    }
                    else if(i==5){
                        del_medicine_info();
                    }
                    else if(i==6){

                    }
                    else {
                        printf("\n\t\t\t\t\tWrong choice!!\n");
                    }
                    printf("\n\t\t\t   Press 'y' to select other choice. Press 'n' for back to main menu.");
                    cha = getche();
                    printf("\n");
                }while(cha=='y');
                break;
            case 5:
                do{
                    system("cls");
                    system("COLOR 09");
                    printf("\n\n");
                    printf("\n\t\t\t--------------<< WELCOME TO CHECK CUSTOMER'S INFO MENU >>--------------\n\n");
                    printf("\t\t\t\t--------------------\n");
                    printf("\t\t\t\t1. To Search Info by ID\n");
                    printf("\t\t\t\t2. To Display All Info\n");
                    printf("\t\t\t\t3. To Edit Info by ID\n");
                    printf("\t\t\t\t4. To Sort Info by ID\n");
                    printf("\t\t\t\t5. To Delete Info by ID\n");
                    printf("\t\t\t\t6. To Back to main menu\n");
                    printf("\t\t\t\t--------------------\n");
                    printf("\t\t\t\tSelect your choice :");
                    scanf("%d", &j);
                    if(j==1){
                        search_customer_info();
                    }
                    else if(j==2){
                        check_customer_info();
                    }
                    else if(j==3){
                        update_customer_info();
                    }
                    else if(j==4){
                        printf("\n");
                        sort_customer_info();
                        printf("\n\t\t\t---------------------<< SORT LIST SUCCESSFUL >>------------------------\n");
                    }
                    else if(j==5){
                        del_customer_info();
                    }
                    else if(j==6){

                    }
                    else {
                        printf("\n\t\t\t\t\tWrong choice!!\n");
                    }
                    printf("\n\t\t\t   Press 'y' to select other choice. Press 'n' for back to main menu.");
                    cha = getche();
                    printf("\n");
                }while(cha=='y');
                break;
            case 6:
                do{
                    system("cls");
                    system("COLOR 09");
                    printf("\n\n");
                    printf("\n\t\t\t---------------<< WELCOME TO CHECK SUPPLY'S INFO MENU >>---------------\n\n");
                    printf("\t\t\t\t--------------------\n");
                    printf("\t\t\t\t1. To Search Info by ID\n");
                    printf("\t\t\t\t2. To Display All Info\n");
                    printf("\t\t\t\t3. To Edit Info by ID\n");
                    printf("\t\t\t\t4. To Sort Info by ID\n");
                    printf("\t\t\t\t5. To Delete Info by ID\n");
                    printf("\t\t\t\t6. To Back to main menu\n");
                    printf("\t\t\t\t--------------------\n");
                    printf("\t\t\t\tSelect your choice :");
                    scanf("%d", &k);
                    if(k==1){
                        search_supplies_info();
                    }
                    else if(k==2){
                        check_supplies_info();
                    }
                    else if(k==3){
                        update_supply_info();
                    }
                    else if(k==4){
                        printf("\n");
                        sort_supply_info();
                        printf("\n\t\t\t---------------------<< SORT LIST SUCCESSFUL >>------------------------\n");
                    }
                    else if(k==5){
                        del_supply_info();
                    }
                    else if(k==6){

                    }
                    else {
                        printf("\n\t\t\t\t\tWrong choice!!\n");
                    }
                    printf("\n\t\t\t   Press 'y' to select other choice. Press 'n' for back to main menu.");
                    cha = getche();
                    printf("\n");
                }while(cha=='y');
                break;
            case 7:
                do{
                    system("cls");
                    system("COLOR 09");
                    printf("\n\n");
                    printf("\n\t\t\t-------------------<< WELCOME TO CHECK PAYMENT MENU >>-----------------\n\n");
                    customer_payment();
                    printf("\n\t\t\t   Press 'y' to check other payment. Press 'n' for back to main menu.");
                    cha = getche();
                    printf("\n");
                }while(cha=='y');
                break;
            case 8:
                do{
                    system("cls");
                    system("COLOR 09");
                    printf("\n\n\n\n\t\t\t-----------------<< THANK YOU FOR BUYING IN OUR STORE >>---------------\n\n");
                    rate();
                    printf("\n\t\t\t\tPress 'y' to RATE us again. Press 'n' for back to main menu.");
                    cha = getche();
                    printf("\n");
                }while(cha=='y');
                break;
            case 9:
                break;
            default:
                printf("\n\t\t\t\tYou select the wrong choice!!\n");
                break;
        }
        printf("\n\t\t\tPress 'y' to go back to main program menu. Press any keys to exit program.");
        choice = getche();
    }while (choice == 'y' || choice == 'Y');
    return 0;
}

