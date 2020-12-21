package common;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

public class QueryServlet extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
       doPost(req,resp);
    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String title= request.getParameter("title");
        String date= request.getParameter("date");
        String nid = request.getParameter("nid");
//        System.out.println(title);
//        System.out.println(date);
//        System.out.println(nid);
        QueryNews qn = new QueryNews();
        String content = qn.qContent(nid,title,date);
//        System.out.println("+++++++++++++++++++++"+content);
        request.setAttribute("content",content);
        request.getRequestDispatcher("content.jsp").forward(request,response);
    }
}
