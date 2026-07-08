package FINAL;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Destination {
    private String Company_name, Location, Province, Start_Date, End_Date, Contact, Benefits, Page_Link;
    private int price;
    public Destination(){}

    public Destination(String company_name, String location, String province, String start_Date, String end_Date, String contact, String benefits, String page_Link, int price) {
        this.setCompany_name(company_name);
        this.setLocation(location);
        this.setProvince(province);
        this.setStart_Date(start_Date);
        this.setEnd_Date(end_Date);
        this.setContact(contact);
        this.setBenefits(benefits);
        this.setPage_Link(page_Link);
        this.setPrice(price);
    }

    public String getCompany_name() {
        return Company_name;
    }

    public void setCompany_name(String company_name) {
        Company_name = company_name;
    }

    public String getLocation() {
        return Location;
    }

    public void setLocation(String location) {
        Location = location;
    }

    public String getProvince() {
        return Province;
    }

    public void setProvince(String province) {
        Province = province;
    }

    public String getStart_Date() {
        return Start_Date;
    }

    public void setStart_Date(String start_Date) {
        boolean isValid = false;
        String strDateRegEx = "((18|19|20)[0-9]{2}[\\-.](0[13578]|1[02])[\\-.](0[1-9]|[12][0-9]|3[01]))|(18|19|20)[0-9]{2}[\\-.](0[469]|11)[\\-.](0[1-9]|[12][0-9]|30)|(18|19|20)[0-9]{2}[\\-.](02)[\\-.](0[1-9]|1[0-9]|2[0-8])|(((18|19|20)(04|08|[2468][048]|[13579][26]))|2000)[\\-.](02)[\\-.]29\n";
        if(start_Date.matches(strDateRegEx)){
            SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd");
            try{
                sdf.parse(start_Date);
                isValid = true;
            }catch(ParseException e){
                e.printStackTrace();
            }
        }
        if(isValid) this.Start_Date = start_Date;
        else System.out.println("Invalid input.");
    }
    public String getEnd_Date() {
        return End_Date;
    }

    public void setEnd_Date(String end_Date) {
        boolean isValid = false;
        String strDateRegEx = "((18|19|20)[0-9]{2}[\\-.](0[13578]|1[02])[\\-.](0[1-9]|[12][0-9]|3[01]))|(18|19|20)[0-9]{2}[\\-.](0[469]|11)[\\-.](0[1-9]|[12][0-9]|30)|(18|19|20)[0-9]{2}[\\-.](02)[\\-.](0[1-9]|1[0-9]|2[0-8])|(((18|19|20)(04|08|[2468][048]|[13579][26]))|2000)[\\-.](02)[\\-.]29\n";
        if(end_Date.matches(strDateRegEx)){
            SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd");
            try{
                sdf.parse(end_Date);
                isValid = true;
            }catch(ParseException e){
                e.printStackTrace();
            }
        }
        if(isValid) this.End_Date = end_Date;
        else System.out.println("Invalid input.");
    }

    public String getContact() {
        return Contact;
    }

    public void setContact(String contact) {
        String allCountryRegex = "^(?!(?:\\D*0)+\\D*$)\\(?([0-9]{3})\\)?[-. ]?[0-9]{3}[-. ]?[0-9]{4}$";
        if (!contact.matches(allCountryRegex)){
            this.Contact = contact;
        }
        else System.out.println("Invalid phone numbers");
    }

    public String getBenefits() {
        return Benefits;
    }

    public void setBenefits(String benefits) {
        Benefits = benefits;
    }

    public String getPage_Link() {
        return Page_Link;
    }
    public static boolean validate_page_link(String url){
        String regex = "((http|https)://)(www.)?"
                + "[a-zA-Z0-9@:%._+~#?&/=]"
                + "{2,256}\\.[a-z]"
                + "{2,6}\\b([-a-zA-Z0-9@:%"
                + "._+~#?&/=]*)";
        Matcher matcher = null;
        Pattern pattern = null;
        try {
            pattern = Pattern.compile(regex, Pattern.CASE_INSENSITIVE);
        } catch (IllegalArgumentException e) {
            e.printStackTrace();
        }
        try {
            assert pattern != null;
            matcher = pattern.matcher(url);
        }catch(NullPointerException npe){
            npe.printStackTrace();
        }
        assert matcher != null;
        return matcher.matches();
    }

    public void setPage_Link(String page_Link) {
        if(validate_page_link(page_Link))
            this.Page_Link = page_Link;
        else System.out.println("Invalid format for the page link you entered.");
    }

    public int getPrice() {
        return price;
    }

    public void setPrice(int price) {
        String v_s = String.valueOf(price);
        if (v_s.matches("[0-9]+")){
            this.price = price;
        }
        else System.out.print("Prices can't contain characters/symbols. Try again.");
    }


    @Override
    public String toString() {
        return "Destination:" +
                "Company_name='" + Company_name + '\'' +
                "Location='" + Location + '\'' +
                "Province='" + Province + '\'' +
                "Start_Date='" + Start_Date + '\'' +
                "End_Date='" + End_Date + '\'' +
                "Contact='" + Contact + '\'' +
                "Benefits='" + Benefits + '\'' +
                "Page_Link='" + Page_Link + '\'' +
                "price=" + price;
    }
}
