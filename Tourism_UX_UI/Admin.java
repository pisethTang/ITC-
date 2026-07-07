package FINAL;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Admin extends Person {
    String admin_id;
    String email;
    String contact;
    public Admin(){}
    public Admin(String admin_id, String email, String contact){
        this.setAdmin_id(admin_id);
        this.setContact(contact);
        this.setEmail(email);
    }


    public String getAdmin_id() {
        return admin_id;
    }

    public void setAdmin_id(String admin_id) {

        this.admin_id = admin_id;
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
        return "Admin{" +
                "admin_id='" + admin_id + '\'' +
                ", email='" + email + '\'' +
                ", contact='" + contact + '\'' +
                '}';
    }
}
