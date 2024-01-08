import feedparser, time

URL="https://everyday-com-eat.tistory.com/rss"
RSS_FEED = feedparser.parse(URL)
MAX_POST=4

markdown_text = """

### ![카피바라](capybara.png) everyday commit <span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span> [![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fjinsugyeong&count_bg=%23CBC2D3&title_bg=%23D8C0F1&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)
![GitHub stats](https://github-readme-stats.vercel.app/api?username=jinsugyeong&theme=buefy&show_icons=true)

<br><br>

### ![카피바라](capybara.png) 사용기술
<div style="display:flex; flex-direction:column; align-items:flex-start;">
    <!-- Language -->
    <p><strong>Language & lib ... </strong></p>
    <div>
        <img src="https://img.shields.io/badge/java-007396?style=flat-square&logo=java&logoColor=white"> 
	<img src="https://img.shields.io/badge/node.js-339933?style=flat-square&logo=Node.js&logoColor=white"> 
        <img src="https://img.shields.io/badge/PHP-777BB4?style=flat-square&logo=PHP&logoColor=white">
	<img src="https://img.shields.io/badge/Dart-0175C2?style=flat-square&logo=express&logoColor=white"> 
	
 	<br>
  
	<img src="https://img.shields.io/badge/html5-E34F26?style=flat-square&logo=html5&logoColor=white"> 
        <img src="https://img.shields.io/badge/css-1572B6?style=flat-square&logo=css3&logoColor=white">  
        <img src="https://img.shields.io/badge/javascript-F7DF1E?style=flat-square&logo=javascript&logoColor=black"> 
        <img src="https://img.shields.io/badge/jQuery-0769AD?style=flat-square&logo=jQuery&logoColor=white"/> 
    </div><br>
    <!-- FrameWork -->
    <p><strong>FrameWork</strong></p>
    <div>
        <img src="https://img.shields.io/badge/Spring-6DB33F?style=flat-square&logo=Spring&logoColor=white">  
        <img src="https://img.shields.io/badge/Spring Boot-6DB33F?style=flat-square&logo=Spring&logoColor=white">         
        <img src="https://img.shields.io/badge/bootstrap-7952B3?style=flat-square&logo=bootstrap&logoColor=white"> 
	<img src="https://img.shields.io/badge/express-000000?style=flat-square&logo=express&logoColor=white"> 
        <img src="https://img.shields.io/badge/Flutter-#02569B?style=flat-square&logo=express&logoColor=white"> 
    </div><br>
    <!-- Database -->
    <p><strong>Database</strong></p>
    <div>
        <img src="https://img.shields.io/badge/mysql-4479A1?style=flat-square&logo=mysql&logoColor=white">
        <img src="https://img.shields.io/badge/oracle-F80000?style=flat-square&logo=oracle&logoColor=white">
        <img src="https://img.shields.io/badge/Microsoft SQL Server-F80000?style=flat-square&logo=Microsoft SQL Server&logoColor=white">
    </div><br>
    <!-- Server -->
    <p><strong>Server</strong></p>
    <div>
        <img src="https://img.shields.io/badge/linux-FCC624?style=flat-square&logo=linux&logoColor=black">
        <img src="https://img.shields.io/badge/apache tomcat-F8DC75?style=flat-square&logo=apachetomcat&logoColor=black">
      <img src="https://img.shields.io/badge/JBoss-D0271D?style=flat-square&logo=JBoss&logoColor=white"/>
    </div><br>

    <!-- Version Control -->
    <p><strong>Verson Control</strong></p>
    <div>
        <img src="https://img.shields.io/badge/git-F05032?style=flat-square&logo=git&logoColor=white"> 
        <img src="https://img.shields.io/badge/github-181717?style=flat-square&logo=github&logoColor=white"> 
        <img src="https://img.shields.io/badge/SVN-809CC9?style=flat-square&logo=seat&logoColor=white"/> 
    </div><br>
    <!-- Development Tools -->
    <p><strong>Development Tools</strong></p>
    <div>
      <img src="https://img.shields.io/badge/Eclipse IDE-2C2255?style=flat-square&logo=Eclipse IDE&logoColor=white"/> 
      <img src="https://img.shields.io/badge/Visual Studio Code-007ACC?style=flat-square&logo=Visual Studio Code&logoColor=white"/> 
      <img src="https://img.shields.io/badge/Android Studio-3DDC84?style=flat-square&logo=Eclipse IDE&logoColor=white"/> 
</div><br>
</div>

<br><br>

### ![카피바라](capybara.png) Today I Learned
""" # list of blog posts will be appended here


for idx, feed in enumerate(RSS_FEED['entries']):
    if idx > MAX_POST:
        break
    else:
        feed_date = feed['published_parsed']
        markdown_text += f"[{time.strftime('%Y/%m/%d', feed_date)} - {feed['title']}]({feed['link']}) <br/>\n"

f = open("README.md",mode="w", encoding="utf-8")
f.write(markdown_text)
f.close()
