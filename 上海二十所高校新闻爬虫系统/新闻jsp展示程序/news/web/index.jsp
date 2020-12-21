<%@ page import="common.QueryNews" %><%--
  Created by IntelliJ IDEA.
  User: zsl
  Date: 2017/11/12
  Time: 12:28
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ page import="common.QueryNews" %>
<%@ page import="org.bson.Document" %>
<%@ page import="com.mongodb.client.MongoCursor" %>
<html lang="zh-cn">
    <head>
       <meta  charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <link rel="stylesheet" href="css/bootstrap.css">
       <script language="JavaScript">
          function CS(selObj){
              window.location.href = "index.jsp?nid="+selObj.value;
          }
        </script>
    <title>新闻</title>
  </head>
  <body>
  <div class="container">
      <h1 class="pageheader">WELCOME.News come from Shanghai</h1>
      <form action="index.jsp" class="form-horizontal">
          <input type="text" name="title" class="span2 search-query" placeholder="新闻标题检索"/>
          <button type="submit" class="btn">Search</button>
          <input type="text" name="content" class="span2 search-query" placeholder="新闻全文检索"/>
          <button type="submit" class="btn">Search</button>
          <select name="nid" onchange="CS(this)" class="dropdown">
              <option>chooose school</option>
              <option value="a">复旦大学</option>
              <option value="b">上海交通大学</option>
              <option value="c">同济大学</option>
              <option value="d">华东师范大学</option>
              <option value="e">华东理工大学</option>
              <option value="f">上海大学</option>
              <option value="g">上海财经大学</option>
              <option value="h">上海理工大学</option>
              <option value="i">上海师范大学</option>
              <option value="j">华东政法大学</option>
              <option value="k">上海海洋大学</option>
              <option value="l">上海对外经贸大学</option>
              <option value="m">上海工程技术大学</option>
              <option value="n">上海电力学院</option>
              <option value="o">上海应用技术大学</option>
              <option value="p">上海立信会计金融学院</option>
              <option value="q">上海政法学院</option>
              <option value="r">上海商学院</option>
              <option value="s">上海海关学院</option>
              <option value="t">上海健康医学院</option>
          </select>
      </form>
      <div class="col-md-12">
          <table class="table table-hover">
              <tr>
                  <th class="text-center">Time</th>
                  <th class="text-left">Title</th>
                  <th class="text-center">School</th>
              </tr>
  <%
    MongoCursor<Document> news =null;
    String title = request.getParameter("title");
    String cont = request.getParameter("content");
    String ni = request.getParameter("nid");
    String s =request.getParameter("s");
    if(title==null || title.equals("")){
        if(cont==null || cont.equals("")){
            if(ni==null || ni.equals("")){
                if (s==null || s.equals("")){
                   s="0";
                }
                news = QueryNews.page(s);
                System.out.println(s);
            }else{
                news = QueryNews.queryByNid(ni);
            }
        }else {
            news = QueryNews.qContentTitle(cont);
        }
    }else{
        news = QueryNews.queryByTitle(title);
    }
    int count=0;
    while(news.hasNext()) {
        Document newss = news.next();
        if (!newss.containsKey("title") || !newss.containsKey("content") || !newss.containsKey("nid") || !newss.containsKey("date")){
            System.out.println("can not find ,maybe the db is crazy!!");
            continue;
        }
        String content =newss.get("content").toString();
        String ti =newss.get("title").toString();
        String nid =newss.get("nid").toString();
        String school = QueryNews.judgeSchool(nid);
        String date =newss.get("date").toString();
        if (content==null || content.equals("")|| ti==null || ti.equals("")|| nid==null || nid.equals("") || date==null || date.equals("")){
            continue;
        }
        count++;
    %>
              <tr>
                  <td><strong>
                      <h5 class="text-center"> <%=date %></h5>
                  </strong></td>
                  <td><strong>
                      <h5 class="text-left"><a href="/queryContent?nid=<%=nid %>&title=<%=ti %>&date=<%=date %>" >
                          <%=ti %></a></h5>
                  </strong></td>
                  <td><strong>
                      <h5 class="text-center"> <%=school %></h5>
                  </strong></td>
              </tr>
  <%
    }
    int i;
    int allcount = QueryNews.countNews();
    %>
          </table></div>
          <div class="col-md-8 col-md-push-1">
          <p>全部新闻的页码：
     <%
    for (i=0;i<allcount/15;i++){
     %> <a href="index.jsp?s=<%=i*15+1 %>"><<%=i+1 %>>&nbsp;</a>
   <%
   }
   %>
          </div>

  </p>
      <div class="col-md-3 col-md-push-1"><em>tips:
          当前共有：<%=count %>条新闻<br>
          全部共有：<%=allcount %>条新闻
      </em></div>
  </div>
  </body>
</html>
