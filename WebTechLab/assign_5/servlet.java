



//date 8 march 2022 
//WT lab assignment 5 java servlet


import java.io.*;  
import javax.servlet.*;  
import javax.servlet.http.*;  
import java.sql.*;  
    
public class display extends HttpServlet{    
        public void doGet(HttpServletRequest req, HttpServletResponse res) throws IOException, ServletException{  
            PrintWriter out = res.getWriter();  
            res.setContentType("text/html");  
            out.println("<html><body>");  
            out.println("<title> Bookshop Data </title>");

            try {  
                Class.forName("sun.jdbc.odbc.JdbcOdbcDriver");  
                Connection con = DriverManager.getConnection("jdbc:odbc:mydsn", "system", "pintu");  //change here in your device
                // Here dsnname- mydsn,user id- system(for oracle 10g),password is pintu.  
                
                // query part starts here
                Statement stmt = con.createStatement();  
                ResultSet rs = stmt.executeQuery("select * from bookshop");

                out.println("<table border=1 width=50% height=50%>");  
                out.println("<tr><th>Book_Id</th><th>Book_Name</th><th>Book_Author</th><th>Book_Price</th><tr>");  
                while (rs.next()) 
                {  
                    int n = rs.getint("book_id");  
                    String nm = rs.getString("book_title");  
                    String s = rs.getString("book_author");
                    String pm = rs.getString("book_price");   
                    out.println("<tr><td>" + n + "</td><td>" + nm + "</td><td>" + s +"</td><td>" + pm + "</td></tr>");   
                }  
                out.println("</table>");  
                out.println("</html></body>");  
                con.close();  
        }  

        catch (Exception e) {  
                out.println("error occured ....");  
            }  

        }  
    }  
