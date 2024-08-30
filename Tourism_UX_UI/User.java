package FINAL;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class User extends Person {
    private String user_id;
    private String email;
    private String contact;
    public User(){}
    public User(String user_id, String email, String contact){
        this.setUser_id(user_id);
        this.setContact(contact);
        this.setEmail(email);
    }

    public String getUser_id() {
        return user_id;
    }

    public void setUser_id(String user_id) {

        this.user_id = user_id;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        String regex = "^[A-Za-z0-9+_.-]+@(.+)$";
        /*In this regex, we have added some restrictions on the username part of the email address. Restrictions in the above regex are:
[A-Z] characters allowed
[a-z] characters allowed
[0-9] numbers allowed
Additionally email may contain only dot(.), dash(-) and underscore(_)
Rest all characters are not allowed*/
        Pattern pattern = Pattern.compile(regex);
        Matcher matcher = pattern.matcher(email);
        boolean b = matcher.matches();
        if(b) this.email = email;
        else System.out.println("Invalid email format");
    }

    public String getContact() {
        return contact;
    }

    public void setContact(String contact) {
        String allCountryRegex = "^(\\+\\d{1,3}( )?)?((\\(\\d{1,3}\\))|\\d{1,3})[- .]?\\d{3,4}[- .]?\\d{4}$";


        if(contact.matches(allCountryRegex))
            this.contact = contact;
        else System.out.println("Invalid input.");
    }

    @Override
    public String toString() {
        return "User{" +
                "user_id='" + user_id + '\'' +
                ", email='" + email + '\'' +
                ", contact='" + contact + '\'' +
                '}';
    }

    public static void main(String[] args) {
        User u1 = new User();
        Scanner sc = new Scanner(System.in);
        String d = sc.nextLine();
        u1.setDATE_OF_BIRTH(d);
        System.out.println(u1.getDATE_OF_BIRTH());
    }
}
