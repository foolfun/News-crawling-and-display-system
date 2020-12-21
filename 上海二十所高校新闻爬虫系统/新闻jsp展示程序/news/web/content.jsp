<%--
  Created by IntelliJ IDEA.
  User: zsl
  Date: 2017/11/15
  Time: 17:39
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@page import='common.*' %>
<%@ page import="java.util.Map" %>
<html  lang="zh-cn">
<head>
    <meta  charset="UTF-8">
    <link rel="stylesheet" href="css/bootstrap.css">
    <title>新闻内容</title>
</head>
<body>
<div class="container">
    <h1 class="pageheader"><%=request.getParameter("title") %></h1>
    <p class="text-right"><em><strong>发表学校：<%=QueryNews.judgeSchool(request.getParameter("nid")) %></strong></em>
    &nbsp;&nbsp; &nbsp;&nbsp;<em><strong>发表时间：<%=request.getParameter("date") %></strong></em></p>
    <div class="row">
        <p class="lead"><%=request.getAttribute("content") %></p>
    </div>
</div>
<%

%>
</body>
</html>
