package common;

import com.mongodb.BasicDBObject;
import com.mongodb.client.FindIterable;
import com.mongodb.client.MongoCollection;
import com.mongodb.client.MongoCursor;
import org.bson.Document;

import java.util.regex.Pattern;

public class QueryNews {


    public static MongoCursor<Document> queryNews(){
        MongoCollection<Document> collection = JDBCMongo.connect();
        FindIterable<Document> findIterable = collection.find().sort(new Document("date",-1));
        MongoCursor<Document> mongoCursor = findIterable.iterator();
        return mongoCursor;
    }

    public static int countNews() {
        MongoCursor<Document> mongoCursor = QueryNews.queryNews();
        int count = 0;
        while (mongoCursor.hasNext()) {
            Document newss = mongoCursor.next();
            if (!newss.containsKey("title")) {
                System.out.println("can not find the title");
                continue;
            }
            count++;
        }
        return count;
    }//计数：全部的新闻

    public static MongoCursor<Document>  queryByTitle(String title){
        MongoCollection<Document> collection = JDBCMongo.connect();
        Pattern pattern = Pattern.compile("^.*"+title+".*$", Pattern.CASE_INSENSITIVE);
        FindIterable<Document> findIterable = collection.find(new Document("title",pattern)).sort(new Document("date",-1));
        MongoCursor<Document> mongoCursor = findIterable.iterator();
        return mongoCursor;
    }//通过标题检索

    public static MongoCursor<Document>  queryByNid(String nid){
        MongoCollection<Document> collection = JDBCMongo.connect();
        FindIterable<Document> findIterable = collection.find(new Document("nid",nid)).sort(new Document("date",-1));
        MongoCursor<Document> mongoCursor = findIterable.iterator();
        return mongoCursor;
    }//通过学校检索

    public static MongoCursor<Document>  qContentTitle(String content){
        MongoCollection<Document> collection = JDBCMongo.connect();
        Document doc = new Document("$text", new Document("$search",content));
        FindIterable<Document> findIterable = collection.find(doc).sort(new Document("date",-1));
        MongoCursor<Document> mongoCursor = findIterable.iterator();
        return mongoCursor;
    }//在list里全文检索

    public String  qContent(String nid, String title,String date){
        MongoCollection<Document> collection = JDBCMongo.connect();
        BasicDBObject bdo = new BasicDBObject();
        bdo.put("nid",nid);
        bdo.put("title",title);
        bdo.put("date",date);
        System.out.println(bdo);
        FindIterable<Document> findIterable = collection.find(bdo);
        MongoCursor<Document> mongoCursor = findIterable.iterator();
        while (mongoCursor.hasNext()){
            String  news= mongoCursor.next().getString("content");
            return news;
        }
        return null;
    }//查询内容

    public static MongoCursor<Document> page(String s) {
        int ss = Integer.parseInt(s);
        MongoCollection<Document> collection = JDBCMongo.connect();
        BasicDBObject sort = new BasicDBObject();
        sort.put("date", -1);
        FindIterable<Document> findIterable = collection.find().sort(sort).skip(ss).limit(15);
        MongoCursor<Document> cur = findIterable.iterator();
        return cur;
    }//分页传给前台

    public static String judgeSchool(String nid){
        if (nid.equals("a")) return "复旦大学";
        else if (nid.equals("b")) return "上海交通大学";
        else if (nid.equals("c")) return "同济大学";
        else if (nid.equals("d")) return "华东师范大学";
        else if (nid.equals("e")) return "华东理工大学";
        else if (nid.equals("f")) return "上海大学";
        else if (nid.equals("g")) return "上海财经大学";
        else if (nid.equals("h")) return "上海理工大学";
        else if (nid.equals("i")) return "上海师范大学";
        else if (nid.equals("j")) return "华东政法大学";
        else if (nid.equals("k")) return "上海海洋大学";
        else if (nid.equals("l")) return "上海对外经贸大学";
        else if (nid.equals("m")) return "上海工程技术大学";
        else if (nid.equals("n")) return "上海电力学院";
        else if (nid.equals("o")) return "上海应用技术大学";
        else if (nid.equals("p")) return "上海立信会计金融学院";
        else if (nid.equals("q")) return "上海政法学院";
        else if (nid.equals("r")) return "上海商学院";
        else if (nid.equals("s")) return "上海海关学院";
        else return "上海健康医学院";
    }

    public static void main(String[] agrs) {

//        MongoCursor<Document> cur =queryByTitle("同济");
//        MongoCursor<Document> cur = qContentTitle("同济");
//        int count=0;
//        while (cur.hasNext()) {
//            count ++;
//            Document newss = cur.next();
//            if (!newss.containsKey("title")){
//                System.out.println("5555");
//                continue;
//            }
//            System.out.println(cur.next().get("title").toString());
//        }
//        System.out.println("共有： " + count + "个");

//        page(0);
    }

}
