package common;

import com.mongodb.MongoClient;
import com.mongodb.client.MongoCollection;
import com.mongodb.client.MongoDatabase;
import org.bson.Document;

public class JDBCMongo {
        static MongoCollection<Document> collection;
        public static MongoCollection<Document>  connect(){
            try{
                // 连接到 mongodb 服务
                MongoClient mongoClient= new MongoClient( "localhost" , 27017 );

                // 连接到数据库
                MongoDatabase mongoDatabase = mongoClient.getDatabase("schoolNews");
//                System.out.println("Connect to database successfully"+mongoDatabase);

                //选择集合
                collection = mongoDatabase.getCollection("news");
                System.out.println("集合 news 选择成功");

            }catch(Exception e){
                System.err.println( e.getClass().getName() + ": " + e.getMessage() );
            }
            return collection;
        }

}
