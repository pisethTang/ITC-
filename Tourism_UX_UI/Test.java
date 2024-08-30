package FINAL;


import java.sql.*;
import java.util.HashMap;
import java.util.InputMismatchException;
import java.util.Scanner;

public abstract class Test{

    public final static Scanner sc = new Scanner(System.in);

    public static void display_provinces(HashMap<Integer, String> pro) {
        for (Integer i : pro.keySet()) {
            System.out.printf("%d ---> %-10s%n", i, pro.get(i));
        }
    }
    public static void display_provinces() {
        HashMap<Integer, String> provinces = new HashMap<>();
        provinces.put(1, "keatie");
        provinces.put(2, "kep");
        provinces.put(3, "koh_kong");
        provinces.put(4, "kompong_speu");
        provinces.put(5, "mondulkiri");
        provinces.put(6, "preah_sihanouk");
        provinces.put(7, "pursat");
        provinces.put(8, "ratanakiri");
        provinces.put(9, "siem_reap");
        provinces.put(10, "stueng_treng");
        for (Integer i : provinces.keySet()) {
            System.out.printf("%d ---> %-10s%n", i, provinces.get(i));
        }
    }

    //Srey Pech's part(38-82)
    public static void register_user() {
        String data_base_name = "data_collected";
        String jdbcURL = "jdbc:mysql://localhost:3306/" + data_base_name;
        String db_user = "root";
        String db_password = "tp352002MDBS";


        User u = new User();
        System.out.print("Name: ");
        u.setNAME(sc.nextLine());
        System.out.print("User_id(e.g. e20201566): ");
        u.setUser_id(sc.nextLine());
        System.out.print("DOB(yyyy-mm-dd): ");
        u.setDATE_OF_BIRTH(sc.nextLine());
        System.out.print("Email: ");
        u.setEmail(sc.nextLine());
        System.out.print("Contact: ");
        u.setContact(sc.nextLine());


        Connection connection;
        try {
            connection = DriverManager.getConnection(jdbcURL, db_user, db_password);
            String table_name = "users_only";
            String sql = "INSERT INTO " + table_name + " (NAME, USER_ID, DOB, EMAIL, CONTACT)" +
                    "VALUES (?, ?, ?, ?, ?)";
            assert connection != null;
            PreparedStatement statement = connection.prepareStatement(sql);
            statement.setString(1, u.getNAME());
            statement.setString(2, u.getUser_id());
            try {
                statement.setDate(3, java.sql.Date.valueOf(u.getDATE_OF_BIRTH()));
            } catch (IllegalArgumentException ie) {
                System.out.println("Wrong argument. Please try again.");
                ie.printStackTrace();
                System.exit(0);
            }
            statement.setString(4, u.getEmail());
            statement.setString(5, u.getContact());
            int rows = statement.executeUpdate();
            if (rows > 0) System.out.println("A new user has been inserted successfully.");
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    //Manon's part(85-129)
    public static void register_admin() {
        String data_base_name = "data_collected";
        String jdbcURL = "jdbc:mysql://localhost:3306/" + data_base_name;
        String db_user = "root";
        String db_password = "tp352002MDBS";

        Admin a = new Admin();
        System.out.print("Name: ");
        a.setNAME(sc.nextLine());
        System.out.print("Admin_id(e.g. e20201893): ");
        a.setAdmin_id(sc.nextLine());
        System.out.print("DOB(yyyy-mm-dd): ");
        a.setDATE_OF_BIRTH(sc.nextLine());
        System.out.print("Email: ");
        a.setEmail(sc.nextLine());
        System.out.print("Contact: ");
        a.setContact(sc.nextLine());
        Connection connection;
        try {
            connection = DriverManager.getConnection(jdbcURL, db_user, db_password);
            //NAME, USER_ID, DOB, EMAIL, CONTACT
            String table_name = "admins_only";
            String sql = "INSERT INTO " + table_name + " (Admin_id, Name, DOB, Email, Contact)" +
                    "VALUES (?, ?, ?, ?, ?)";
            assert connection != null;
            PreparedStatement statement = connection.prepareStatement(sql);
            statement.setString(1, a.getNAME());
            statement.setString(2, a.getAdmin_id());
            try {
                statement.setDate(3, java.sql.Date.valueOf(a.getDATE_OF_BIRTH()));
            } catch (IllegalArgumentException ie) {
                System.out.println("Wrong argument. Please try again.");
                ie.printStackTrace();
                System.exit(0);
            }
            statement.setString(4, a.getEmail());
            statement.setString(5, a.getContact());
            int rows = statement.executeUpdate();
            if (rows > 0) System.out.println("A new user has been inserted successfully.");
        } catch (SQLException e) {
            e.printStackTrace();
        }


    }

    public static int row_table(String table_name){
        String data_base_name = "data_collected";
        String jdbcURL = "jdbc:mysql://localhost:3306/" + data_base_name;
        String db_user = "root";
        String db_password = "tp352002MDBS";
        int count = 0;
        Connection connection;
        try {
            connection = DriverManager.getConnection(jdbcURL, db_user, db_password);
            String sql = "SELECT COUNT(*) FROM " + table_name;

            assert connection != null;
            PreparedStatement statement = connection.prepareStatement(sql);

            ResultSet rs = statement.executeQuery();
            rs.next();
            count = rs.getInt(1);
            System.out.println("Number of records: " + count);

        } catch (SQLException e) {
            System.err.println("There is something wrong. Please see below:");
            e.printStackTrace();
        }
        return count;
    }

    //Ratanak's part(158-182)
    public static boolean admin_login(String password_admin_id) throws IllegalArgumentException, SQLException {
        String data_base_name = "data_collected";
        String jdbcURL = "jdbc:mysql://localhost:3306/" + data_base_name;
        String db_user = "root";
        String db_password = "tp352002MDBS";
        Connection connection = null;
        boolean flag_admin = false; // admin' id is in the  database or not?
        try {
            //get connection to mysql
            connection = DriverManager.getConnection(jdbcURL, db_user, db_password);
            String table_name = "admins_only";
            String sql = "SELECT * FROM " + table_name + " WHERE Admin_id='" + password_admin_id + "'";
            PreparedStatement statement = connection.prepareStatement(sql);
            ResultSet rs = statement.executeQuery();
            if (rs.next()) flag_admin = true;
        } catch (SQLException e1) {
            System.err.println("Something went wrong...please see instructions below.");
            e1.printStackTrace();


        }
        assert connection != null;
        connection.close();
        return flag_admin;
    }

    //Nary's part(185-205)
    public static boolean user_login(String password_user_id) throws IllegalArgumentException, SQLException {
        String data_base_name = "data_collected";
        String jdbcURL = "jdbc:mysql://localhost:3306/" + data_base_name;
        String db_user = "root";
        String db_password = "tp352002MDBS";
        Connection connection = null;
        boolean flag_user = false;
        try {
            connection = DriverManager.getConnection(jdbcURL, db_user, db_password);
            String table_name = "users_only";
            String sql = "SELECT * FROM " + table_name + " WHERE USER_ID='" + password_user_id + "'";
            PreparedStatement statement = connection.prepareStatement(sql);
            ResultSet rs = statement.executeQuery();
            if (rs.next()) flag_user = true;
        } catch (SQLException e) {
            e.printStackTrace();
        }
        assert connection != null;
        connection.close();
        return flag_user;
    }


    //------------------------------------ MY PART -------------------------------------------------
    public static void add_destination_record(String table_name) {
        String data_base_name = "data_collected";
        String jdbcURL = "jdbc:mysql://localhost:3306/" + data_base_name;
        String db_user = "root";
        String db_password = "tp352002MDBS";


        Destination d = new Destination();
        System.out.print("Company name: ");
        d.setCompany_name(sc.nextLine());
        System.out.print("Location: ");
        d.setLocation(sc.nextLine());
        System.out.print("Province: ");
        d.setProvince(sc.nextLine());
        System.out.print("Price($/person): ");
        d.setPrice(sc.nextInt());
        sc.nextLine();
        System.out.print("Start date: ");
        d.setStart_Date(sc.nextLine());
        System.out.print("End date: ");
        d.setEnd_Date(sc.nextLine());
        System.out.print("Contact: ");
        d.setContact(sc.nextLine());
        System.out.print("Benefits/Offers: ");
        d.setBenefits(sc.nextLine());
        System.out.print("Page links: ");
        d.setPage_Link(sc.nextLine());

        Connection connection;
        try {
            connection = DriverManager.getConnection(jdbcURL, db_user, db_password);
            String sql = "INSERT INTO " + table_name + " (`Company_Name`, `Location`, `Province`, `Price`, `Start_Date`, `End_Date`, `Tel`, `Benefits`, `Page_Link`)" +
                    " VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)";
            assert connection != null;
            PreparedStatement statement = connection.prepareStatement(sql);
            statement.setString(1, d.getCompany_name());
            statement.setString(2, d.getLocation());
            statement.setString(3, d.getProvince());
            statement.setInt(4, d.getPrice());
            try {
                statement.setDate(5, java.sql.Date.valueOf(d.getStart_Date()));
                statement.setDate(6, java.sql.Date.valueOf(d.getEnd_Date()));
            } catch (IllegalArgumentException ie) {
                System.out.println("Wrong argument. Please try again.");
                ie.printStackTrace();
                System.exit(0);
            }
            statement.setString(7, d.getContact());
            statement.setString(8, d.getBenefits());
            statement.setString(9, d.getPage_Link());
            int rows = statement.executeUpdate();
            System.out.println(rows);
            if (rows > 0) System.out.println("A new destination record has been inserted successfully.");
            else System.out.println("Something wrong");
        } catch (SQLException e) {
            System.err.println("There is something wrong. Please see below:");
            e.printStackTrace();
        }
    } // 7
    public static void delete_user_record(int ID_user) {
        String data_base_name = "data_collected";
        String jdbcURL = "jdbc:mysql://localhost:3306/" + data_base_name;
        String db_user = "root";
        String db_password = "tp352002MDBS";
        Connection connection;

        try {
            connection = DriverManager.getConnection(jdbcURL, db_user, db_password);
            String table_name = "users_only";
            String sql = "DELETE FROM " + table_name + " WHERE ID=?";
            PreparedStatement statement = connection.prepareStatement(sql);
            statement.setInt(1, ID_user);
            //statement.setString(1, user_name);
            int rows = statement.executeUpdate();
            if (rows > 0) {
                System.out.println("The user with ID " +ID_user+ " has been deleted from the database.");
            } else {
                System.out.println("User ID "+ ID_user+ " is not in the database.");
            }
            connection.close();
        } catch (SQLException e) {
            e.printStackTrace();
        }

    }
    public static void delete_admin_record(int ID_admin) {
        String data_base_name = "data_collected";
        String jdbcURL = "jdbc:mysql://localhost:3306/" + data_base_name;
        String db_user = "root";
        String db_password = "tp352002MDBS";
        Connection connection;

        try {
            connection = DriverManager.getConnection(jdbcURL, db_user, db_password);
            String table_name = "admins_only";
            String sql = "DELETE FROM " + table_name + " WHERE username=?";
            PreparedStatement statement = connection.prepareStatement(sql);

            statement.setInt(1, ID_admin);
            int rows = statement.executeUpdate();
            if (rows > 0) {
                System.out.println("The user with ID " +ID_admin+ " has been deleted from the database.");
            } else {
                System.out.println("User ID "+ ID_admin+ " is not in the database.");
            }
            connection.close();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
    public static void delete_destination_record(String table_name, int dest_id) {
        String data_base_name = "data_collected";
        String jdbcURL = "jdbc:mysql://localhost:3306/" + data_base_name;
        String db_user = "root";
        String db_password = "tp352002MDBS";

        Connection connection;
        try {
            connection = DriverManager.getConnection(jdbcURL, db_user, db_password);
            String sql = "DELETE FROM " + table_name + " WHERE ID = ?";
            assert connection != null;
            PreparedStatement statement = connection.prepareStatement(sql);
            statement.setInt(1, dest_id);
            int rows = statement.executeUpdate();
            if (rows > 0) System.out.println("Destination record ID: " + dest_id + " has been deleted successfully.");
            else System.out.println("Please check everything again.");
        } catch (SQLException e) {
            System.err.println("There is something wrong. Please see below:");
            e.printStackTrace();
        }
    }
    public static void update_user(String user_id) throws NullPointerException {
        String data_base_name = "data_collected";
        String jdbcURL = "jdbc:mysql://localhost:3306/" + data_base_name;
        String db_user = "root";
        String db_password = "tp352002MDBS";
        Connection connection;


        User u = new User();
        System.out.print("Name: ");
        u.setNAME(sc.nextLine());
        System.out.print("User_id(e.g. e20201566): ");
        u.setUser_id(sc.nextLine());
        System.out.print("DOB(yyyy-mm-dd): ");
        u.setDATE_OF_BIRTH(sc.nextLine());
        System.out.print("Email: ");
        u.setEmail(sc.nextLine());
        System.out.print("Contact: ");
        u.setContact(sc.nextLine());


        try {
            connection = DriverManager.getConnection(jdbcURL, db_user, db_password);
            String table_name = "users_only";
            String sql = "UPDATE " + table_name + " SET NAME=?, USER_ID=?, DOB=?, EMAIL=?, CONTACT=? WHERE ID=?";
            PreparedStatement statement = connection.prepareStatement(sql);
            statement.setString(1, u.getNAME());
            statement.setString(2, u.getUser_id());
            statement.setString(3, u.getDATE_OF_BIRTH());
            statement.setString(4, u.getEmail());
            statement.setString(5, u.getContact());
            statement.setString(6, user_id);

            int rows = statement.executeUpdate();
            if (rows > 0) {
                System.out.println("The user's information has been updated!");
                connection.close();
            } else {
                System.out.println("""
                        Error during the updating process. Possible reasons:\s
                        - Grammatical and punctuation errors.
                        - The specified user's id is not in our database.""");
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }

    }

    public static void update_admin(String admin_id) throws NullPointerException {
        String data_base_name = "data_collected";
        String jdbcURL = "jdbc:mysql://localhost:3306/" + data_base_name;
        String db_user = "root";
        String db_password = "tp352002MDBS";
        Connection connection;

        Admin a = new Admin();
        System.out.print("Name: ");
        a.setNAME(sc.nextLine());
        System.out.print("Admin_id(e.g. e20201893): ");
        a.setAdmin_id(sc.nextLine());
        System.out.print("DOC(yyyy-mm-dd): ");
        a.setDATE_OF_BIRTH(sc.nextLine());
        System.out.print("Email: ");
        a.setEmail(sc.nextLine());
        System.out.print("Contact: ");
        a.setContact(sc.nextLine());

        try {
            String table_name = "admins_only";
            connection = DriverManager.getConnection(jdbcURL, db_user, db_password);
            String sql = "UPDATE " + table_name + " SET Admin_id=?, Name=?, DOB=?, Email=?, Contact=? WHERE ID=?";
            PreparedStatement statement = connection.prepareStatement(sql);
            statement.setString(1, a.getAdmin_id());
            statement.setString(2, a.getNAME());
            statement.setString(3, a.getDATE_OF_BIRTH());
            statement.setString(4, a.getEmail());
            statement.setString(5, a.getContact());
            statement.setString(6, admin_id);
            int rows = statement.executeUpdate();
            if (rows > 0) {
                System.out.println("The admins' with the name " + a.getNAME() + "  information has been updated!");
                connection.close();
            } else {
                System.out.println("""
                        Error during the updating process. Possible reasons:\s
                        - Grammatical and punctuation errors.
                        - The specified admins' id is not in our database.""");
            }

        } catch (SQLException e) {
            e.printStackTrace();
        }


    }

    public static void update_destination(String table_name, int id_destination) {
        String data_base_name = "data_collected";
        String jdbcURL = "jdbc:mysql://localhost:3306/" + data_base_name;
        String db_user = "root";
        String db_password = "tp352002MDBS";



        Destination d = new Destination();
        System.out.print("Company name: ");
        d.setCompany_name(sc.nextLine());
        System.out.print("Location: ");
        d.setLocation(sc.nextLine());
        System.out.print("Province: ");
        d.setProvince(sc.nextLine());
        System.out.print("Price($/person): ");
        d.setPrice(sc.nextInt());
        sc.nextLine();
        System.out.print("Start date: ");
        d.setStart_Date(sc.nextLine());
        System.out.print("End date: ");
        d.setEnd_Date(sc.nextLine());
        System.out.print("Contact: ");
        d.setContact(sc.nextLine());
        System.out.print("Benefits/Offers: ");
        d.setBenefits(sc.nextLine());
        System.out.print("Page links: ");
        d.setPage_Link(sc.nextLine());

        Connection connection;
        try {
            connection = DriverManager.getConnection(jdbcURL, db_user, db_password);
            String sql = "INSERT INTO " + table_name + " (`Company_Name`, `Location`, `Province`, `Price($/1person)`, `Start_Date`, `End_Date`, `Tel`, `Benefits`, `Page_Link`)" +
                    " VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?) WHERE ID=?";
            assert connection != null;
            PreparedStatement statement = connection.prepareStatement(sql);
            statement.setString(1, d.getCompany_name());
            statement.setString(2, d.getLocation());
            statement.setString(3, d.getProvince());
            statement.setInt(4, d.getPrice());
            try {
                statement.setDate(5, java.sql.Date.valueOf(d.getStart_Date()));
                statement.setDate(6, java.sql.Date.valueOf(d.getEnd_Date()));
            } catch (IllegalArgumentException ie) {
                System.out.println("Wrong argument. Please try again.");
                ie.printStackTrace();
                System.exit(0);
            }
            statement.setString(7, d.getContact());
            statement.setString(8, d.getBenefits());
            statement.setString(9, d.getPage_Link());
            statement.setInt(10, id_destination);
            int rows = statement.executeUpdate();
            if (rows > 0) System.out.println("The destination record with ID: "+id_destination+" has been updated successfully.");
        } catch (SQLException e) {
            System.err.println("There is something wrong. Please see below:");
            e.printStackTrace();
        }
    }//2
    public static void search_users(int options) {
        String data_base_name = "data_collected";
        String jdbcURL = "jdbc:mysql://localhost:3306/" + data_base_name;
        String db_user = "root";
        String db_password = "tp352002MDBS";
        Connection connection;

        String table_name = "users_only";
        String sql;

        try {
            connection = DriverManager.getConnection(jdbcURL, db_user, db_password);
            boolean working = true;
            while(working){
                switch(options){
                    case 1 -> { // order by ID(1,2,...)
                        System.out.println("Ascending or descending order?(1/0)");
                        int ch = sc.nextInt();
                        sc.nextLine();
                        if(ch == 1) {
                            sql = "SELECT * FROM " + table_name + " ORDER BY ID ASC";
                            execute_result_set(connection, sql);
                        }
                        else if(ch == 0) {
                            sql = "SELECT * FROM " + table_name + " ORDER BY ID DESC";
                            execute_result_set(connection, sql);
                        }
                    }
                    case 2 -> { //by name
                        System.out.println("Enter an admin name: ");
                        String s = sc.nextLine();
                        sql = "SELECT * FROM " + table_name + " WHERE NAME REGEXP '"+s+"'"
                                +" OR NAME REGEXP '^" + s + "' OR NAME REGEXP '"+s+"$'";
                        execute_result_set(connection, sql);
                    }
                    case 3 -> { //Admin_id
                        System.out.println("Enter an admin id: ");
                        String s1 = sc.nextLine();
                        sql = "SELECT * FROM " + table_name + " WHERE USER_ID REGEXP '"+s1+"'"
                                +" OR NAME REGEXP '^" + s1 + "' OR NAME REGEXP '"+s1+"$'";
                        execute_result_set(connection, sql);
                    }
                    //given the time, we can try to think of more options,
                    default -> {
                        System.out.println("Invalid option. Try again.");
                    }
                }
                System.out.println("Do you want to continue?(1 -> y/0 ->n)");
                int h = 0;
                try{
                    h = sc.nextInt();
                    sc.nextLine();
                }catch(InputMismatchException m){
                    m.printStackTrace();
                }
                if(h == 1) working = false;
            }

        } catch (SQLException e) {
            System.err.println("There is something wrong. Please see below:");
            e.printStackTrace();
        }
        System.out.print("Press enter to continue:");
        sc.nextLine();
    } //3
    public static void execute_result_set(Connection connection, String sql) throws SQLException {
        String d1 = "Company_Name";
        String d2 = "Location";
        String d3 = "Province";
        String d4 = "Price";
        String d5 = "Start_date";
        String d6 = "End_date";
        String d7 = "Tel";
        String d8 = "Benefits";
        String d9 = "Page_Link";
        assert connection != null;
        PreparedStatement statement = connection.prepareStatement(sql);
        ResultSet rs = statement.executeQuery();
        System.out.printf("%-5s%-35s%-45s%-30s%-20s%-15s%-15s%-20s%-70s%-70s%n",
                "ID", d1, d2, d3, d4, d5, d6, d7+"(+855)", d8, d9);
        int i = 1;
        while (rs.next()) {
            String s_d = null, e_d = null;
            try {
                s_d = String.valueOf(rs.getDate(d5));
                e_d = String.valueOf(rs.getDate(d6));
            }catch(SQLSyntaxErrorException se){
                System.out.println("Something's wrong...");
                se.printStackTrace();
            }
            System.out.printf("%-5d%-35s%-45s%-30s%-20d%-15s%-15s%-20s%-70s%-70s%n", i, rs.getString(d1), rs.getString(d2), rs.getString(d3),
                    rs.getInt(d4), s_d,e_d, rs.getString(d7), rs.getString(d8), rs.getString(d9));
            i++;
        }
    }
    public static void search_admins(int options) {
        String data_base_name = "data_collected";
        String jdbcURL = "jdbc:mysql://localhost:3306/" + data_base_name;
        String db_user = "root";
        String db_password = "tp352002MDBS";
        Connection connection;

        String table_name = "admins_only";
        String sql;



        try {
            connection = DriverManager.getConnection(jdbcURL, db_user, db_password);
            boolean working = true;
            while(working){
                switch(options){
                    case 1 -> { // order by ID(1,2,...)
                        System.out.println("Ascending or descending order?(1/0)");
                        int ch = sc.nextInt();
                        sc.nextLine();
                        if(ch == 1) {
                            sql = "SELECT * FROM " + table_name + " ORDER BY ID ASC";
                            execute_result_set(connection, sql);
                        }
                        else if(ch == 0) {
                            sql = "SELECT * FROM " + table_name + " ORDER BY ID DESC";
                            execute_result_set(connection, sql);
                        }
                    }
                    case 2 -> { //by name
                        System.out.println("Enter an admin name: ");
                        String s = sc.nextLine();
                        sql = "SELECT * FROM " + table_name + "WHERE Name REGEXP '"+s+"'"
                                +" OR " + table_name + " REGEXP '^" + s + "' OR " + table_name+ " REGEXP " + table_name+ "'"+s+"$'";
                        execute_result_set(connection, sql);
                    }
                    case 3 -> { //Admin_id
                        System.out.println("Enter an admin id: ");
                        String s1 = sc.nextLine();
                        sql = "SELECT * FROM " + table_name + "WHERE Admin_id REGEXP '"+s1+"'"
                                +" OR " + table_name + " REGEXP '^" + s1 + "' OR " + table_name+ " REGEXP " + table_name+ "'"+s1+"$'";
                        //insert regular expression codes over here....
                        execute_result_set(connection, sql);

                    }
                    //given the time, we can try to think of more options,
                    default -> {
                        System.out.println("Invalid option. Try again.");
                    }
                }
                System.out.println("Do you want to continue?(1 -> y/0 ->n)");
                int h = 0;
                try{
                    h = sc.nextInt();
                    sc.nextLine();
                }catch(InputMismatchException m){
                    m.printStackTrace();
                }
                if(h == 1) working = false;
            }

        } catch (SQLException e) {
            System.err.println("There is something wrong. Please see below:");
            e.printStackTrace();
        }
        System.out.print("Press enter to continue:");
        sc.nextLine();
    }
    //search manually
    public static void search_destinations(String table_name, int c) { // search manually
        String data_base_name = "data_collected";
        String jdbcURL = "jdbc:mysql://localhost:3306/" + data_base_name;
        String db_user = "root";
        String db_password = "tp352002MDBS";

        Connection connection;
        String sql;
        try {
            connection = DriverManager.getConnection(jdbcURL, db_user, db_password);
            switch(c){
                case 1 -> { // order by price
                    System.out.println("Ascending or descending order?(1/0)");
                    int ch = sc.nextInt();
                    sc.nextLine();
                    //get max/min/average price
                    if(ch == 1) {
                        sql = "SELECT * FROM " + table_name + " ORDER BY Price ASC";
                        execute_result_set(connection, sql);
                    }
                    else if(ch == 0) {
                        sql = "SELECT * FROM " + table_name + " ORDER BY Price DESC";
                        execute_result_set(connection, sql);
                    }
                }
                case 2 -> { //location
                    System.out.println("Enter a location: ");
                    System.out.print("SEARCH BAR: ");
                    String s = sc.nextLine();

                    sql = "SELECT * FROM " + table_name + " WHERE Location REGEXP '"+s+"'"
                            +" OR Location REGEXP '^" + s + "' OR Location REGEXP '"+s+"$'" + " OR Location REGEXP '[a-z]' OR Location REGEXP '[0-9]'";

                    //insert regular expression codes over here....
                    execute_result_set(connection, sql);
                }
                case 3 -> { //date
                    System.out.println("""
                            Do you want to view destinations available:
                            1_ this month(December)
                            2_ 1 month from now(January)
                            3_ 2 months from now(February)
                            """);
                    int choice = 0;
                    try {
                        choice = sc.nextInt();
                        sc.nextLine();
                    }catch(InputMismatchException v){
                        System.out.println("Input should only be one of the number specified.");
                        v.printStackTrace();
                    }
                    if(choice == 1){ // Decémbre
                        sql = "SELECT * FROM " + table_name +
                                " WHERE Start_Date BETWEEN '2022-12-01' AND '2022-12-31'";
                        execute_result_set(connection, sql);
                    }
                    else if(choice ==2){ // Janviér
                        sql = "SELECT * FROM " + table_name +
                                " WHERE Start_Date BETWEEN '2023-01-01' AND '2023-01-31'";
                        execute_result_set(connection, sql);
                    }
                    else if(choice == 3){ // Février
                        sql = "SELECT * FROM " + table_name +
                                " WHERE Start_Date BETWEEN '2022-02-01' AND '2022-02-28'";
                        execute_result_set(connection, sql);
                    }
                    else{
                        System.out.println("Invalid input. Try again.");
                    }
                }
                case 4 -> { //company_name
                    System.out.println("Enter a company name: ");
                    System.out.print("SEARCH BAR: ");
                    String s1 = sc.nextLine();

                    sql = "SELECT * FROM " + table_name + " WHERE Company_Name REGEXP '"+s1+"'"
                            +" OR Company_Name REGEXP '^" + s1 + "' OR Company_Name REGEXP '"+s1+"$'" + " OR Company_Name REGEXP 'Der2' OR Company_Name REGEXP '^ad' OR Company_Name REGEXP '[0-9]'";
                    //they can either enter the name of the provinces or enter partially the province's name partially...also insert regular expression code over here
                    execute_result_set(connection, sql);
                }
                //given the time, we can try to think of more options,
                default -> {
                    System.out.println("Invalid option. Try again.");
                }

                }

        } catch (SQLException e) {
            System.err.println("There is something wrong. Please see below:");
            e.printStackTrace();
        }
    }
    //search through everything
    public static void search_destinations(int o) {
        String data_base_name = "data_collected";
        String jdbcURL = "jdbc:mysql://localhost:3306/" + data_base_name;
        String db_user = "root";
        String db_password = "tp352002MDBS";


        String table_name = "every_province";
        Connection connection;
        String sql;
        try {
            connection = DriverManager.getConnection(jdbcURL, db_user, db_password);
            switch(o){
                case 1 -> { // order by price
                    System.out.println("Ascending or descending order?(1/0)");
                    int ch = sc.nextInt();
                    sc.nextLine();
                    //get max/min/average price of everything or of each table
                    if(ch == 1) {
                        sql = "SELECT * FROM " + table_name + " ORDER BY Price ASC";
                        execute_result_set(connection, sql);
                    }
                    else if(ch == 0) {
                        sql = "SELECT * FROM " + table_name + " ORDER BY Price DESC";
                        execute_result_set(connection, sql);
                    }
                }
                case 2 -> { //location
                    System.out.println("Enter a location: ");
                    System.out.print("SEARCH BAR: ");
                    String s = sc.nextLine();

                    sql = "SELECT * FROM " + table_name + " WHERE Location REGEXP '"+s+"'"
                            +" OR  Location REGEXP '^" + s + "' OR Location REGEXP '"+s+"$' ";
                    execute_result_set(connection, sql);
                }
                case 3 -> { //date
                    System.out.println("""
                            Do you want to view destinations available:
                            1_ this month(December)
                            2_ 1 month from now(January)
                            3_ 2 months from now(February)
                            """);
                    int choice = 0;
                    try {
                        choice = sc.nextInt();
                        sc.nextLine();
                    }catch(InputMismatchException v){
                        System.out.println("Input should only be one of the number specified.");
                        v.printStackTrace();
                    }
                    if(choice == 1){ // Decémbre
                        sql = "SELECT * FROM " + table_name +
                                " WHERE Start_Date BETWEEN '2022-12-01' AND '2022-12-31'";
                        execute_result_set(connection, sql);
                    }
                    else if(choice ==2){ // Janviér
                        sql = "SELECT * FROM " + table_name +
                                " WHERE Start_Date BETWEEN '2023-01-01' AND '2023-01-31'";
                        execute_result_set(connection, sql);
                    }
                    else if(choice == 3){ // Février
                        sql = "SELECT * FROM " + table_name +
                                " WHERE Start_Date BETWEEN '2022-02-01' AND '2022-02-28'";
                        execute_result_set(connection, sql);
                    }
                    else{
                        System.out.println("Invalid input. Try again.");
                    }
                }
                case 4 -> { //company_name
                    System.out.println("Enter a company: ");
                    System.out.print("SEARCH BAR: ");
                    String s1 = sc.nextLine();
                    sql = "SELECT * FROM " + table_name + " WHERE Company_Name REGEXP '"+s1+"'"
                            +" OR Company_Name REGEXP '^" + s1 + "' OR Company_Name REGEXP '"+s1+"$' ";
                    execute_result_set(connection, sql);
                }
                //given the time, we can try to think of more options,
                default -> {
                    System.out.println("Invalid option. Try again.");
                }
            }
        } catch (SQLException e) {
            System.err.println("There is something wrong. Please see below:");
            e.printStackTrace();
        }
    }

    public static void display_users() {
        String data_base_name = "data_collected";
        String jdbcURL = "jdbc:mysql://localhost:3306/" + data_base_name;
        String db_user = "root";
        String db_password = "tp352002MDBS";
        Connection connection;
        String c1 = "NAME";
        String c2 = "USER_ID";
        String c3 = "DOB";
        String c4 = "EMAIL";
        String c5 = "CONTACT";



        try {
            connection = DriverManager.getConnection(jdbcURL, db_user, db_password);
            String table_name = "users_only";
            String sql = "SELECT * FROM " + table_name;
            PreparedStatement statement = connection.prepareStatement(sql);
            ResultSet rs = statement.executeQuery();
            System.out.printf("\n%-5s%-15s%-15s%-15s%-50s%-25s%n", "ID", c1, c2, c3, c4, c5);
            int i = 1;
            while (rs.next()) {
                System.out.printf("%-5d%-15s%-15s%-15s%-50s%-25s%n", i,
                        rs.getString(c1), rs.getString(c2), rs.getString(c3),
                        rs.getString(c4), rs.getString(c5));
                i++;
            }
        } catch (SQLException e) {
            System.err.println("Uh oh...");
            e.printStackTrace();
        }
    }

    public static void display_admins() {
        String data_base_name = "data_collected";
        String jdbcURL = "jdbc:mysql://localhost:3306/" + data_base_name;
        String db_user = "root";
        String db_password = "tp352002MDBS";
        Connection connection;
        String c1 = "NAME";
        String c2 = "ADMIN_ID";
        String c3 = "DOB";
        String c4 = "EMAIL";
        String c5 = "CONTACT";
        try {
            connection = DriverManager.getConnection(jdbcURL, db_user, db_password);
            String table_name = "admins_only";
            String sql = "SELECT * FROM " + table_name;
            PreparedStatement statement = connection.prepareStatement(sql);
            ResultSet rs = statement.executeQuery();
            System.out.printf("\n%-5s%-15s%-15s%-15s%-50s%-25s\n", "ID", c1, c2, c3, c4, c5);
            int i = 1;
            while (rs.next()) {
                System.out.printf("%-5d%-15s%-15s%-15s%-50s%-25s%n", i,
                        rs.getString(c1), rs.getString(c2), rs.getString(c3),
                        rs.getString(c4), rs.getString(c5));
                i++;
            }
        } catch (SQLException e) {
            System.err.println("Uh oh...");
            e.printStackTrace();
        }
    }

    public static void display_destinations(String table_name) {
        String data_base_name = "data_collected";
        String jdbcURL = "jdbc:mysql://localhost:3306/" + data_base_name;
        String db_user = "root";
        String db_password = "tp352002MDBS";

        String d1 = "Company_Name";
        String d2 = "Location";
        String d3 = "Province";
        String d4 = "Price";
        String d5 = "Start_date";
        String d6 = "End_date";
        String d7 = "Tel";
        String d8 = "Benefits";
        String d9 = "Page_Link";


        Connection connection;
        try {
            connection = DriverManager.getConnection(jdbcURL, db_user, db_password);
            String sql = "SELECT * FROM " + table_name;
            assert connection != null;
            PreparedStatement statement = connection.prepareStatement(sql);
            ResultSet rs = statement.executeQuery();
            System.out.printf("%-5s%-35s%-45s%-30s%-20s%-15s%-15s%-20s%-70s%-70s%n",
                    "ID", d1, d2, d3, d4, d5, d6, d7+"(+855)", d8, d9);
            int i = 1;
            while (rs.next()) {
                String s_d = null, e_d = null;
                try {
                    s_d = String.valueOf(rs.getDate(d5));
                    e_d = String.valueOf(rs.getDate(d6));
                }catch(SQLSyntaxErrorException se){
                    System.out.println("Something's wrong...");
                    se.printStackTrace();
                }
                System.out.printf("%-5d%-35s%-45s%-30s%-20d%-15s%-15s%-20s%-70s%-70s%n", i, rs.getString(d1), rs.getString(d2), rs.getString(d3),
                        rs.getInt(d4), s_d,e_d, rs.getString(d7), rs.getString(d8), rs.getString(d9));
                i++;
            }
        } catch (SQLException e) {
            System.err.println("There is something wrong. Please see below:");
            e.printStackTrace();
        }
        System.out.print("Press enter to continue:");
        sc.nextLine();



    } //6

    /*6 more functions to go*/
    public static void main(String[] args) throws SQLException, InputMismatchException {
        Scanner sc = new Scanner(System.in);
        HashMap<Integer, String> provinces = new HashMap<>();
        provinces.put(1, "keatie");
        provinces.put(2, "kep");
        provinces.put(3, "koh_kong");
        provinces.put(4, "kompong_speu");
        provinces.put(5, "mondulkiri");
        provinces.put(6, "preah_sihanouk");
        provinces.put(7, "pursat");
        provinces.put(8, "ratanakiri");
        provinces.put(9, "siem_reap");
        provinces.put(10, "stueng_treng");
        int num_tables = provinces.size();
        System.out.println("""
                ==================================
                | Tourism Recommendation Program |
                ==================================
                """);
        boolean flag = true;
        try {
            while (flag) {
                System.out.println("======================MAIN MENU===========================");
                System.out.print("Are you a user or admin?: ");
                String u_a = sc.nextLine();
                //user
                if (u_a.equalsIgnoreCase("user")) {
                    System.out.print("Have you registered yet?(y/n or yes/no): ");
                    String choice = sc.nextLine();
                    if (choice.equalsIgnoreCase("y") || choice.equalsIgnoreCase("yes")) {
                        System.out.println("You will be redirected to the login page...");
                        System.out.print("Enter your user_id(case_sensitive): ");
                        if (user_login(sc.nextLine())) { // user logged in
                            System.out.println("===============Successful login!=================");
                            System.out.print("Press enter to continue");
                            sc.nextLine();
                            boolean working = true;
                            while(working){
                            System.out.println("==============================SEARCH==================================");
                            System.out.print("Do you want to search through all the provinces at once or not?(1/0): ");
                            int c_c = sc.nextInt();
                            try {
                                sc.nextLine();
                            }catch (Exception m){
                                System.out.println("Error");
                                m.printStackTrace();
                            }
                            if(c_c == 0){ // search province manually
                                    display_provinces();
                                    int options = 0;
                                    try {
                                        System.out.print("Enter a number according to the province(1-10): ");
                                        options = sc.nextInt();
                                        sc.nextLine();
                                    }catch(InputMismatchException m){
                                        System.out.println("Wrong Argument!!!");
                                        m.printStackTrace();
                                    }
                                    if(options >= 1 && options <= provinces.size()) {
                                        System.out.print("""
                                                Search by:
                                                1. Price
                                                2. Location
                                                3. Date
                                                4. Company_Name
                                                Enter an option(1-4):""");
                                        int field = 0;
                                        try {
                                            field = sc.nextInt();
                                            sc.nextLine();
                                        } catch (InputMismatchException i) {
                                            i.printStackTrace();
                                        }
                                        if (field == 0) {
                                            System.out.println("Invalid input!");
                                        } else search_destinations(provinces.get(options), field);
                                        System.out.print("Do you want to continue?(1 -> y/0 ->n)");
                                        int h = 0;
                                        try {
                                            h = sc.nextInt();
                                            sc.nextLine();
                                        } catch (InputMismatchException ime) {
                                            System.out.println("Please enter only 1 or 0");
                                            ime.printStackTrace();
                                        }
                                        if (h == 0) {
                                            System.out.println("You will be redirected back to the main menu.");
                                            working = false;
                                        }
                                    }
                                    else{
                                        System.out.println("Invalid input!");
                                    }
                                }
                            else if(c_c == 1){ // search through everything
                                    System.out.print("""
                                    Search by:
                                    1. Price
                                    2. Location
                                    3. Date
                                    4. Company_Name
                                    Enter an option(1-4):""");
                                    int options = 0;
                                    try {
                                        options = sc.nextInt();
                                        sc.nextLine();
                                    }catch(InputMismatchException m){
                                        System.out.println("Wrong Argument!!!");
                                        m.printStackTrace();
                                    }
                                    if(options >= 1 && options <= 4){
                                        search_destinations(options);
                                        System.out.print("Do you want to continue?(1 -> y/0 ->n)");
                                        int h = 0;
                                        try{
                                            h = sc.nextInt();
                                            sc.nextLine();
                                        }catch(InputMismatchException ime){
                                            System.out.println("Please enter only 1 or 0");
                                            ime.printStackTrace();
                                        }
                                        if (h == 0) {
                                            System.out.println("You will be redirected back to the main menu.");
                                            working = false;
                                        }                                    }
                                    else{
                                        System.out.println("Invalid input!");
                                    }
                                }
                            }
                        }

                        else {
                            System.out.println("Invalid login, check your user_ID again.");
                            System.out.println("You will be redirected to the home page.");
                        }
                    } else if (choice.equalsIgnoreCase("n") || choice.equalsIgnoreCase("no")) {
                        System.out.println("====== USER REGISTRATION PAGE ======");
                        register_user();
                    } else {
                        System.out.println("Invalid input! Try again.");
                    }

                }


                //Admin
                else if (u_a.equalsIgnoreCase("admin")) {
                    System.out.print("Enter your admin_ID(case-sensitive): ");
                    if (admin_login(sc.nextLine())) { // admin logged in
                        System.out.println("Congrats! You are logged in.");
                        System.out.print("Press enter to continue...");
                        sc.nextLine();
                        System.out.println("""
                                1. Add admin
                                2. Add user
                                3. Add destination_information
                                4. Display destination information
                                5. Display user information
                                6. Display admin information
                                7. Search destination information (price,...etc)
                                8. Search user information
                                9. Search  admin information
                                10. Delete destination information
                                11. Delete admin information
                                12. Delete user information
                                13. Update destination information
                                14. Update admin information
                                15. Update user information
                                16. Exit the program
                                """);
                        System.out.print("Choose one of the above: ");
                        String ch = sc.nextLine();
                        switch (ch) {
                            case "1" -> register_admin();
                            case "2" -> register_user();
                            case "3" -> {
                                System.out.println("=============================ADD DESTINATION RECORD========================");
                                display_provinces(provinces);
                                System.out.print("Choose one of the tables above to be modified(1-" + num_tables + "): ");
                                int t_name = sc.nextInt();
                                sc.nextLine();
                                if(provinces.containsKey(t_name)){
                                    add_destination_record(provinces.get(t_name));
                                }else System.out.println("Table specified is not within our database.");
                            }
                            case "4" -> {
                                System.out.println("========================Display Destination Record========================");
                                display_provinces(provinces);
                                System.out.print("Which province do you want to see?(1-" + num_tables + "): ");
                                int t_name = sc.nextInt();
                                sc.nextLine();
                                if(provinces.containsKey(t_name)){
                                    display_destinations(provinces.get(t_name));
                                }else System.out.println("Table specified is not within our database.");
                            }
                            case "5" -> {
                                System.out.println("========================Display User Record========================");
                                display_users();
                                System.out.print("Press Enter to continue: ");
                                sc.nextLine();
                            }
                            case "6" -> {
                                System.out.println("========================Display Admin Record========================");
                                display_admins();
                                System.out.print("Press Enter to continue: ");
                                sc.nextLine();
                            }
                            case "7" -> {
                                System.out.println("========================Search Destination Record========================");
                                boolean working = true;
                                while(working){
                                    System.out.println("==============================SEARCH==================================");
                                    System.out.print("Do you want to search through all the provinces at once or not?(1/0): ");
                                    int c_c = sc.nextInt();
                                    try {
                                        sc.nextLine();
                                    }catch (Exception m){
                                        System.out.println("Error");
                                        m.printStackTrace();
                                    }
                                    if(c_c == 0){ // search province manually
                                        display_provinces();
                                        int options = 0;
                                        try {
                                            System.out.print("Enter a number according to the province(1-10): ");
                                            options = sc.nextInt();
                                            sc.nextLine();
                                        }catch(InputMismatchException m){
                                            System.out.println("Wrong Argument!!!");
                                            m.printStackTrace();
                                        }
                                        if(options >= 1 && options <= provinces.size()) {
                                            System.out.print("""
                                                Search by:
                                                1. Price
                                                2. Location
                                                3. Date
                                                4. Company_Name
                                                Enter an option(1-4):""");
                                            int field = 0;
                                            try {
                                                field = sc.nextInt();
                                                sc.nextLine();
                                            } catch (InputMismatchException i) {
                                                i.printStackTrace();
                                            }
                                            if (field == 0) {
                                                System.out.println("Invalid input!");
                                            } else search_destinations(provinces.get(options), field);
                                            System.out.print("Do you want to continue?(1 -> y/0 ->n)");
                                            int h = 0;
                                            try {
                                                h = sc.nextInt();
                                                sc.nextLine();
                                            } catch (InputMismatchException ime) {
                                                System.out.println("Please enter only 1 or 0");
                                                ime.printStackTrace();
                                            }
                                            if (h == 0) {
                                                System.out.println("You will be redirected back to the main menu.");
                                                working = false;
                                            }
                                        }
                                        else{
                                            System.out.println("Invalid input!");
                                        }
                                    }
                                    else if(c_c == 1){ // search through everything
                                        System.out.print("""
                                    Search by:
                                    1. Price
                                    2. Location
                                    3. Date
                                    4. Company_Name
                                    Enter an option(1-4):""");
                                        int options = 0;
                                        try {
                                            options = sc.nextInt();
                                            sc.nextLine();
                                        }catch(InputMismatchException m){
                                            System.out.println("Wrong Argument!!!");
                                            m.printStackTrace();
                                        }
                                        if(options >= 1 && options <= 4){
                                            search_destinations(options);
                                            System.out.print("Do you want to continue?(1 -> y/0 ->n)");
                                            int h = 0;
                                            try{
                                                h = sc.nextInt();
                                                sc.nextLine();
                                            }catch(InputMismatchException ime){
                                                System.out.println("Please enter only 1 or 0");
                                                ime.printStackTrace();
                                            }
                                            if (h == 0) {
                                                System.out.println("You will be redirected back to the main menu.");
                                                working = false;
                                            }                                    }
                                        else{
                                            System.out.println("Invalid input!");
                                        }
                                    }
                                }
                            }
                            case "8" -> {
                                System.out.println("=========================Search User Record========================");
                                System.out.println("""
                                        Search by:
                                        1. ID(1,2,3...)
                                        2. Name
                                        3. User_id(e2020...)
                                        Choose one(1-3):
                                        """);
                                int options = 0;
                                try {
                                    options = sc.nextInt();
                                }catch(InputMismatchException m){
                                    System.out.println("Wrong Argument!!!");
                                    m.printStackTrace();
                                }
                                sc.nextLine();
                                if(options >= 1 && options <= 4){
                                    search_users(options);
                                }
                                else{
                                    System.out.println("Invalid input!");
                                }
                                System.out.print("Press Enter to continue: ");
                                sc.nextLine();
                            }
                            case "9" -> {
                                System.out.println("=========================Search Admin Record========================");
                                System.out.println("""
                                        Search by:
                                        1. ID(1,2,3...)
                                        2. Name
                                        3. Admin_id(e2020...)
                                        Choose one(1-3):
                                        """);
                                int options = 0;
                                try {
                                    options = sc.nextInt();
                                }catch(InputMismatchException m){
                                    System.out.println("Wrong Argument!!!");
                                    m.printStackTrace();
                                }
                                sc.nextLine();
                                if(options >= 1 && options <= 4){
                                    search_admins(options);
                                }
                                else{
                                    System.out.println("Invalid input!");
                                }
                                System.out.print("Press Enter to continue: ");
                                sc.nextLine();
                            }
                            case "10" -> {
                                System.out.println("========================Delete Destination Record========================");
                                display_provinces(provinces);
                                System.out.print("Choose one of the tables above to be modified(1-" + num_tables + "): ");
                                int t_name_del = 0;
                                try {
                                    t_name_del = sc.nextInt();
                                    sc.nextLine();
                                    if(provinces.containsKey(t_name_del)) continue;
                                    else{
                                        System.out.println("The table specified is not within our database.");
                                        System.exit(0);
                                    }
                                }catch (IllegalArgumentException e) {
                                    System.err.println("Wrong argument!");
                                    e.printStackTrace();
                                }
                                display_destinations(provinces.get(t_name_del));
                                System.out.print("Enter the destination ID that you want to delete: ");
                                int des_id = 0;
                                try {
                                    des_id = sc.nextInt();
                                }catch (InputMismatchException e){
                                    System.out.println("Wrong argument.");
                                    e.printStackTrace();
                                }
                                if (des_id >= 1 && des_id <= row_table(provinces.get(t_name_del))) {
                                    delete_destination_record(provinces.get(t_name_del), des_id);
                                    System.out.print("Press Enter to continue: ");
                                    sc.nextLine();
                                }
                                else System.out.println("The table specified is not within our database.");
                            }
                            case "11" -> {
                                System.out.println("====================================Delete admin record==============================================");
                                display_admins();
                                System.out.print("Enter the user ID to be deleted(1,2...): ");
                                int user_i = 0;
                                try {
                                    user_i = sc.nextInt();
                                }catch (InputMismatchException m){
                                    System.out.println("WRONG INPUT!");
                                    m.printStackTrace();
                                }
                                sc.nextLine();
                                delete_admin_record(user_i);
                                System.out.print("Press Enter to continue: ");
                                sc.nextLine();
                            }
                            case "12" -> {
                                System.out.println("====================================Delete user record==============================================");
                                display_users();
                                System.out.print("Enter the user ID to be deleted(1,2...): ");
                                int admin_i = 0;
                                try {
                                    admin_i = sc.nextInt();
                                }catch(InputMismatchException m){
                                    System.out.println("WRONG INPUT!!");
                                    m.printStackTrace();
                                }
                                sc.nextLine();
                                delete_user_record(admin_i);
                                System.out.print("Press Enter to continue: ");
                                sc.nextLine();
                            }
                            case "13" -> {
                                System.out.println("===============UPDATE DESTINATION RECORD===============");
                                display_provinces(provinces);
                                System.out.print("Which table do you want to look at?:");
                                int table_dest = sc.nextInt();
                                sc.nextLine();
                                if(provinces.containsKey(table_dest)){
                                    display_destinations(provinces.get(table_dest));
                                    System.out.print("Enter the destination ID that you want to update:");
                                    int des_id = sc.nextInt();
                                    sc.nextLine();
                                    if (des_id >= 1 && des_id <= row_table(provinces.get(table_dest))) {
                                        update_destination(provinces.get(table_dest), des_id);
                                        System.out.print("Press Enter to continue: ");
                                        sc.nextLine();
                                    }
                                    else {
                                        System.out.println("Record with ID " + des_id + " doesn't exist.");
                                    }
                                }
                                else System.out.println("The table specified is not in our database.");

                            }
                            case "14" -> {
                                System.out.println("===============================Update Admin' Record====================================");
                                System.out.print("Enter an admin' id to modify his/her data(1,2,....): ");
                                int u_id = 0;
                                try {
                                    u_id = sc.nextInt();
                                }catch(InputMismatchException m){
                                    System.out.println("Wrong input!!");
                                    m.printStackTrace();
                                }
                                sc.nextLine();
                                String user_table = "admins_only";
                                //validate
                                if(u_id >= 0 && u_id <=row_table(user_table)) {
                                    System.out.println("Now enter the id as in (e20...)");
                                    String u = sc.nextLine();
                                    update_user(u);
                                }else System.out.println("The specified ID doesn't exist.");
                                System.out.print("Press Enter to continue: ");
                                sc.nextLine();
                            }
                            case "15" -> {
                                System.out.println("===============================Update User's Record====================================");
                                String admin_table = "users_only";
                                System.out.print("Enter a user's id to modify his/her data(1,2,....): ");
                                int a_id = 0;
                                try {
                                    a_id = sc.nextInt();
                                }catch (InputMismatchException m){
                                    System.out.println("Wrong input!!!");
                                    m.printStackTrace();
                                }
                                sc.nextLine();
                                //validate
                                if(a_id >= 0 && a_id <=row_table(admin_table)) {
                                    System.out.println("Now enter the id as in (e20...)");
                                    String a = sc.nextLine();
                                    update_admin(a);
                                }else System.out.println("The specified ID doesn't exist.");

                                System.out.print("Press Enter to continue: ");
                                sc.nextLine();
                            }
                            default -> {
                                System.out.print("Are you sure you want to exit?(y/n)");
                                String c = sc.nextLine();
                                if (c.matches("[a-zA-Z]+")) {
                                    if (c.equalsIgnoreCase("y")) {
                                        System.out.println("Program exiting...........");
                                        Loading.printMsgWithProgressBar("Loading", 50, 60);
                                        flag = false;
                                    } else if (c.equalsIgnoreCase("n")) {
                                        System.out.println("Please continue.");
                                    } else {
                                        System.out.println("Invalid response.");
                                    }
                                } else System.out.println("Answer must either be y or n. Try again.");
                            }
                        }

                    } else {
                        System.out.println("Invalid login, check your user_ID again.");
                        System.out.println("You will be redirected to the home page.");
                    }

                } else {
                    System.out.println("Try again.");
                }
            }
            System.exit(0);
        }catch (Exception in){
            System.out.println("Something wrong with the process. Check the trace below....");
            in.printStackTrace();
        }

    }
}
