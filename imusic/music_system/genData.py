from .models import user, artist, music, album
from django.utils import timezone

from random import randint, choice, random
from datetime import datetime

from django.contrib.auth.models import User, Group, Permission


# config
USER_NUM = 10
ARTIST_NUM = 10

MUSIC_NUM = 30

ALBUM_NUM = 10

# attr data config
names = ['Anthony', 'Arthur', 'Austin', 'Ben', 'Benson', 'Bill', 'Bob', 'Brandon', 'Brant', 'Brent', 'Brian', 'Bruce', 'Carl', 'Cary', 'Caspar', 'Charles', 'Cheney', 'Chris', 'Christian', 'Christopher', 'Colin', 'Cosmo', 'Daniel', 'Dennis', 'Derek', 'Donald', 'Douglas', 'David', 'Denny', 'Edgar', 'Edward', 'Edwin', 'Elliott', 'Elvis', 'Eric', 'Evan', 'Francis', 'Frank', 'Franklin', 'Fred', 'Gabriel', 'Gaby', 'Garfield', 'Gary', 'Gavin', 'George', 'Gino', 'Glen', 'Glendon', 'Harrison', 'Hugo', 'Hunk', 'Howard', 'Henry', 'Ignativs', 'Ivan', 'Isaac', 'Jack', 'Jackson', 'Jacob', 'James', 'Jason', 'Jeffery', 'Jerome', 'Jerry', 'Jesse', 'Jim', 'Jimmy', 'Joe', 'John', 'Johnny', 'Joseph', 'Joshua', 'Justin', 'Keith', 'Ken', 'Kenneth', 'Kenny', 'Kevin', 'Lance', 'Larry', 'Laurent', 'Lawrence', 'Leander', 'Lee', 'Leo', 'Leonard', 'Leopold', 'Loren', 'Lori', 'Lorin', 'Luke', 'Marcus', 'Marcy', 'Mark', 'Marks', 'Mars', 'Martin', 'Matthew', 'Michael', 'Mike', 'Neil', 'Nicholas', 'Oliver', 'Oscar', 'Paul', 'Patrick', 'Peter', 'Philip', 'Phoebe', 'Quentin', 'Randall', 'Randolph', 'Randy', 'Reed', 'Rex', 'Richard', 'Richie', 'Robert', 'Robin', 'Robinson', 'Rock', 'Roger', 'Roy', 'Ryan', 'Sam', 'Sammy', 'Samuel', 'Scott', 'Sean', 'Shawn', 'Sidney', 'Simon', 'Solomon', 'Spark', 'Spencer', 'Spike', 'Stanley', 'Steven', 'Stuart', 'Terence', 'Terry', 'Timothy', 'Tommy', 'Tom', 'Thomas', 'Tony', 'Tyler', 'Van', 'Vern', 'Vernon', 'Vincent', 'Warren', 'Wesley', 'William', 'Abigail', 'Abby', 'Ada', 'Adelaide', 'Adeline', 'Alexandra', 'Ailsa', 'Aimee', 'Alice', 'Alina', 'Allison', 'Amanda', 'Amy', 'Amber', 'Anastasia', 'Andrea', 'Angela',
         'Angelia', 'Angelina', 'Ann', 'Anne', 'Annie', 'Anita', 'Ariel', 'April', 'Ashley', 'Aviva', 'Barbara', 'Beata', 'Beatrice', 'Becky', 'Betty', 'Blanche', 'Bonnie', 'Brenda', 'Camille', 'Candice', 'Carina', 'Carmen', 'Carol', 'Caroline', 'Carry', 'Carrie', 'Cassandra', 'Cassie', 'Catherine', 'Cathy', 'Chelsea', 'Charlene', 'Charlotte', 'Cherry', 'Cheryl', 'Chris', 'Christina', 'Christine', 'Christy', 'Cindy', 'Claudia', 'Clement', 'Cloris', 'Connie', 'Constance', 'Cora', 'Corrine', 'Crystal', 'Daisy', 'Daphne', 'Darcy', 'Debbie', 'Deborah', 'Debra', 'Demi', 'Diana', 'Dolores', 'Donna', 'Doris', 'Edith', 'Editha', 'Elaine', 'Eleanor', 'Elizabeth', 'Ella', 'Ellen', 'Ellie', 'Emerald', 'Emily', 'Emma', 'Enid', 'Elsa', 'Erica', 'Estelle', 'Esther', 'Eudora', 'Eva', 'Eve', 'Fannie', 'Fiona', 'Frances', 'Frederica', 'Frieda', 'Gina', 'Gillian', 'Gladys', 'Gloria', 'Grace', 'Greta', 'Gwendolyn', 'Hannah', 'Helena', 'Hellen', 'Hebe', 'Heidi', 'Ingrid', 'Ishara', 'Irene', 'Iris', 'Ivy', 'Jacqueline', 'Jamie', 'Jane', 'Janet', 'Jean', 'Jessica', 'Jessie', 'Jennifer', 'Jenny', 'Jill', 'Joan', 'Joanna', 'Jocelyn', 'Josephine', 'Josie', 'Joy', 'Joyce', 'Judith', 'Judy', 'Julia', 'Juliana', 'Julie', 'June', 'Karen', 'Karida', 'Katherine', 'Kate', 'Kathy', 'Katrina', 'Kay', 'Kelly', 'Kitty', 'Lareina', 'Laura', 'Lena', 'Lydia', 'Lillian', 'Linda', 'Lisa', 'Liz', 'Lorraine', 'Louisa', 'Louise', 'Lucia', 'Lucy', 'Lucine', 'Lulu', 'Lynn', 'Maggie', 'Mamie', 'Manda', 'Mandy', 'Margaret', 'Mariah', 'Martha', 'Mary', 'Matilda', 'Maureen', 'Mavis', 'Maxine', 'May', 'Mayme', 'Megan', 'Melinda', 'Melissa', 'Melody', 'Mercedes', 'Meredith']

jokes = ['虞姬说：“大王我想活。”霸王说：“可是外面有十万人马呢，他们若抓了你……”虞姬：“十万人我也忍得了，我还是想活。”霸王哭了：“十万人马，还有马呢……”虞姬含泪“大王，这不是还有你嘛”\r', ' 开学没几天口腔溃疡了。一开始忍了几天，后来都没法吃饭。\r晚自习时老爸带我去医院挂急诊。 好不容易等到我，刚张开嘴，\r医生就大喊：“别看了，口腔溃疡晚期！” 一听到“晚期”我爸腿都软了。\r然后医生慢慢说：“快好了，别浪费钱了。” \r', ' 现在小学生真惹不起！那天上班要迟到了，看见前面一辆出租车刚从小区出来，\r我一个箭步冲了上去！看见一个背包的小学生坐在上面；\r我急忙说道：“小弟弟，姐姐上班要迟到了，你等下一辆行吗？”\r那小学生不屑的说道：“我上学还要迟到了呢！”\r这把我气得！对司机喊道：“我出50！先送我！”\r小学生也喊道：“我出100！先送我！”\r我又喊道：“我特么出200！先送我！”\r小学生淡定的说道：“你赢了！爸，你先送她吧！” \r', '“爸，我跟你说个事……” “怎么了？” “爸，我……我是同性恋。” “卧槽你不会喜欢我吧！？”\r', '早上去买包子还剩三个我特意只买两个；\r老板说:最后一个算了送你了然后回家跟老婆炫耀我是怎么省钱的。\r第二天发现家里快被包子堆满了。\r见我儿子说:爸，我学你买包子去了，我去包子铺问有多少个包子\r老板说:281个我就买了280个，老板二话不说把剩下的包子给我了。\r', '在妈妈的逼迫下和她高中同学的儿子相亲了。\r到饭店一看，感觉有点显老又不帅，于是我立马点了根烟：我这个人什么都好，就一点不好，喜欢和各种男的出去约。\r然后抽着烟看着他，我们年轻人的事你别和我妈妈说，我当你是朋友。\r这时一个帅气的小伙子从厕所走过来，惊愕：爸，这就是和我相亲的？\r', '晚饭后 ，女儿缠着爸爸说:“爸爸,让我亲一下.”爸爸听了很高兴,忙把脸凑过去,问道：“是不是觉得爸爸对你特别好啊？”女儿在爸爸脸上来回亲了好几下,然后说道：“嗯，这下嘴巴擦干净了.家里餐巾纸没了,下次去超市别忘了买。”\r', '幼儿园开学，许多孩子被送来，家长走后，孩子们哭闹着，简直跟宰猪场差不多！这时候，唯独有一个小孩蹲在墙角巨蛋定，老师准备好好夸一下他，刚走近，那个小孩以迅雷不及掩耳之势，抢过老师手机，连号码都没拨，拿起手机就对着手机哭喊着：爸爸，快来救我啊！我被妈妈卖了！\r', '今天我，儿子，老公看电视时老公学电视里给我来了一个排山倒海，不巧的时刚好大姨妈来了，我准备去厕所是裤子上以经染了，然后儿子大叫“爸爸你把我妈妈打伤了”！然后儿子偏要老公教他！\r', '爸爸和儿子在看电视，有接吻的镜头就对儿子说：“去给我倒杯水。”过了一会又有接吻的镜头又让儿子倒水，儿子说：“爸爸，你看到别人亲嘴就口渴啊！”\r', '我们这里的冬天很冷，人人都出门都捂得严严实实的，那天老公开车，我坐旁边，儿子坐后面，一个老太太前面蹬个三轮车，挡在老公车前面，老公生气骂开了：“个老比东西，晃晃悠悠的！”车开过去，儿子回头看了一眼说：“爸爸，是奶奶！”\r', '小新说：“老师，我家人很喜欢动物；爷爷爱河马，奶奶爱猫，妈妈爱兔，妹妹爱鱼，我爱大象。”\r老师问：“你爸爸呢？”\r小新说：“我爸爸很特别，他爱狐狸精！ ”\r', '妈妈：美美，瞧你爸多能干啊，这次又把坏掉的冰箱修好了。你爸什么都会修，大到家电，小到鞋子丶包包.....只有你想不到，没有他修不好。美美“是啊，爸爸好厉害！太棒了！等我长大了，也要嫁一个像爸爸这样的男人。妈妈：得了吧！嫁个这样的，你一辈子也别想用上新东西。\r', '我要出去闯闯！下定决心后告诉爸爸，\r爸爸说：年轻人闯闯也是应该的，别到时给家里打电话说几天没吃饭了。\r我：.........（想问问是不是亲生的）\r', '女儿要买糖，就去找妈妈要钱。妈妈担心吃糖多了对孩子牙齿不好，就开玩笑似的对女儿说：“闺女，咱家没钱，你要买糖，就把你爸爸卖了换钱吧！”\r女儿一听，大哭起来，听得我心里暖暖的——贴身小棉袄，不白疼女儿。\r越哭声音越高，还抽抽噎噎的边哭边说：“人家都有爸爸，谁买我爸爸呀？”\r', '2、妈妈向小女儿安妮详细讲解了小宝宝是怎样来到这个世界的。小安妮静默了一会儿妈妈于是问她：“你明白了吗？”\r“是的。”\r“还有什么问题吗？”\r“是的，那我们的小猫咪呢？也是这样来的吗？”\r“对，跟小宝宝一样啊。”\r“哇！”安妮兴奋地大叫，“我爸爸好棒，什么事都会做！”\r', '夜深人静，小李躲在被窝用平板电脑看岛国片。\r片里的演员正在剧烈运动，但却发不出任何声响，把音量调至最大也无济于事。\r就在小李琢磨自己平板电脑为什么播不出声音的时候有人敲了他房间门。\r爸妈不是睡觉了吗？小李内心想着。\r这时房间的门打开，爸爸将蓝牙音箱丢还给了他。\r', '爸爸心粗，经常丢三落四，妈妈心细，做事井井有条，所以家里的事必须妈妈“领导”爸爸。 于是，爸爸就成了甩手掌柜的。    爸爸经常玩笑妈妈：“在你手下打工不但没工钱，每月还得交份子钱，这也就算了，咋还要扣押我身份证，难道还怕老头纸跑了不成？……     妈妈说:“别得了便宜卖乖，看把你脦涩的，打明儿个起，份子钱按天计算！”\r', '小儿子刚满7岁，一天小儿子问爸爸:为什么哥哥要叫李解放么？\r爸爸:啊，这个呀。咱们村有个风俗，就是孩子刚生下来，爸爸出门看到的第一个东西，就拿这个东西给小孩命名。\r儿子:哦。\r爸爸:当时生你哥的时候门口将好有一辆解放牌自行车，所以你哥哥就叫做李解放，知道了么，狗屎。\r', '风景区买了个诸葛亮的扇子。。\r路上一小女孩指着我说：爸爸快来看，济 公。。\r', '爸爸妈妈带着阿呆去加利福尼亚的海滩度假。海滩上的老外们都一丝不挂的裸泳。阿呆：爸爸，你的鸡鸡怎么没有那些叔叔的大？爸爸：......因为......那些叔叔比爸爸有钱。过了一会儿。阿呆想喝可乐，爸爸一人去上店里买。阿呆和妈妈留在海滩，可是爸爸回来后发现妈妈不见了。爸爸：你妈妈呢？阿呆：爸爸，你刚走后，来了一个很有钱的叔叔，他看着我妈妈，钱是越来越多越来越多，后来我妈妈就跟他走了。\r', '小蚊子哭着从戏院回到家。妈妈问：“怎么了宝贝？”小蚊子说：“爸爸没了。”妈妈问：“出现了啥情况？你爸爸是怎么没的？”小蚊子说：“戏到高潮，人家拍巴掌，爸爸一不小心，躲闪不及被打死了。”\r', '“爸爸去哪儿”很火，戏中的爸爸各种体贴、认真和温柔，小孩犯错过从不打骂，而是耐心地讲各种道理解……弄得全国爸爸都倍感压力，其实tmd都是在演戏!\r', '一位刚刚荣升的上校到前线视察他将要接管的部队，他走到队列中一位有点羞涩的士兵面前时停了下来，说：“小伙子，头抬高点，即使在大人物面前也要挺起胸来。让我们握握手。你可以写信告诉家里，说你同上校握过手，他们一定会为此感到骄做的。小伙子，你爸爸是什么人？” \r“报告长官，我爸爸是将军。” \r', '上幼儿园的儿子一回到家就大喊。\r儿子：“爸爸！爸爸！我要骂你！”\r爸爸惊讶：“臭小子！你想挨揍吗？”\r儿子：“我要骂你！小朋友们也要骂你！因为老师要骂你！”\r最后爸爸弄明白了，幼儿园要收书本费。\r巧的是，老师今天教了一个英文单词money。\r', '今晚和老婆正办着大事，儿子在睡梦中被惊醒了，他问了一句爸爸妈妈你们干什么的？我答了一句和你妈练功的，三岁的儿子从被窝里一下就站起来了，说了句爸爸我也练。当场无言以对\r', '殡仪馆内开出一辆殡 仪车，一小孩追着车大哭：老爸老爸你别走。。\r周围的人很同情，正想去安慰，这时殡仪车停下了，司机下车对小孩说：不要闹了，爸爸下了班 带你 去玩。。\r', '某人看见路边有一瞎眼男子带着孩子乞讨，很同情上去给了些钱，并问孩子：你爸爸眼睛是怎吗瞎的啊？\r孩子回答：是听别人说装成残废可以赚到很多钱所以才‘瞎’了的……\r某人无语……\r', '爸爸是样猪不是因为它像动画片里可爱，而是要吃它的肉，养鸭是为了吃鸭肉，养鸡是为了吃鸡肉，那爸爸我为什么要样我呢？\r', ' 今天下午，我家妹子放学啦，她对我舅舅说：“爸比，我是从哪里来的啊？”\r此时我心想：又是一个经典的问题啊然后她爸愣是跟她解释了半个多小时，\r最后只见她一脸疑惑的说：“我是这样来的吗？可是我们班的小雅说她是云南来的。”\r我已笑喷 \r', '一朋友老婆出差，有个三岁的孩子，他带孩子去公园玩，给孩子身上放个移动WIFI。\r他就坐旁边玩手机，一旦信号弱了，就说明孩子走远了……  \r', '爸妈25年结婚纪念日，我发短信祝福老爸老妈：爸妈结婚纪念日快乐！25年前请客不带我，25年后我也赶不回去。。。。本想煽情一下，结果老爸说，25年前你在场啊，在你妈肚子里。。。。\r', '王尼玛：“我觉得我爸妈特有想象力。”\r曹尼玛:“为什么？”\r王尼玛：“我问我是咋来的事后他们都说我是捡来的”\r曹尼玛:“那有什么稀奇，很多爸妈都这么说。”\r王尼玛：“关键是他们说我是打怪捡来的。。。。。。。。”\r', '春节假期，一家人去三亚旅游。酒店住的套房，爸妈睡大床，我睡客厅沙发。半夜音乐听见规律的啪啪声。我以为老妈白天太累，老爸帮她按捶腰呢。就随口问了一句，结果我妈说没有，还说是下雨的声音吧。。。然后我瞬间明白了，爸妈啊，你们身体是多么好，玩了一天了不累吗\r', '我都十几了，爸妈还是那么火热。\r今天路过爸妈房间听到以下对话：妈：老公你为什么爱我？\r爸：爱你不需要理由的！\r妈：不行，你得说！\r爸：我爱你温柔贤惠漂亮勤劳！\r妈：这不就对了，也不要把我说的这么好啦。\r爸：那你把刀放下，咱好好说话行不',' 一天爸妈在客厅看《步步惊心》，我爸说：“哎，你看那个人不是以前小虎队那谁吗？”我妈：“嗯，是啊，叫什么名字来着？”我爸：“好像。。。。对了，隆力奇！对对，就是他０\r', '男：“我喜欢你！”\r女：“你是喜欢我这个人呢？还是喜欢我爸妈造我的过程？”\r', '今天在家看封神英雄传。\r妈：“你看这妖精和神仙就是有区别，妖精永远都是坏的。”\r爸：“妖精哪里坏了，也有好的。”\r妈：“妖精哪里有好的，你看这狐狸精多坏！”\r爸：“鸡精和味精就挺好的！”\r', '一次放学回家，买了包烟打算晚上偷偷抽。\r刚到家我爸就说：“下楼给我买包烟！”\r我家住六楼没电梯所以赖的下去。\r我脑残的来了句：“爸你先抽我的吧！”\r果然，我被抽了！\r']


music_names = '''完美主义,星晴,娘子,斗牛,黑色幽默,伊斯坦堡,印地安老斑鸠,龙卷风,反方向的钟,爸,简单爱,忍者,开不了口,上海,对不起,威廉古堡,双截棍,安静,半岛铁盒,暗号,龙拳,火车叨位去,分裂,爷爷泡的茶,回到过去,米兰的小铁匠,最后的战役,懦夫,晴天,三年二班,东风破,你听得到,同一种调调,她的睫毛,爱情悬崖,梯田,双刀,七里香,借口,外婆,将军,搁浅,乱舞春秋,困兽之斗,园游会,止战之殇,蓝色风暴,发如雪,黑色毛衣,四面楚歌,枫,浪漫手机,逆鳞,麦芽糖,珊瑚海,飘移,一路向北,听妈妈的话,千里之外,本草纲目,退后,红磨坊,心雨,白色风车,迷迭香,菊花台,彩虹,青花瓷,阳光宅男,蒲公英的约定,无双,我不配,扯,甜甜的,最长的电影,给我一首歌的时间,蛇舞,花海,魔术先生,说好的幸福呢,兰亭序,流浪诗人,时光机,乔克叔叔,稻香,说了再见,烟花易冷,免费教学录影带,好久不见,雨下一整晚,嘻哈空姐,我落泪・情绪零碎,爱的飞行日记,自导自演,超人不会飞,迷魂曲,MineMine,公主病,你好吗,疗伤烧肉粽,琴伤,水手怕水,世界未末日,皮影戏,超跑女神,手语,公公偏头痛,明明就,傻笑,比较大的大提琴,爱你没差,红尘客栈,梦想启动,大笨钟,哪里都是你,乌克丽丽,窃爱,算什么男人,天涯过客,怎么了,一口气全念对,我要夏天,手写的从前,鞋子特大号,听爸爸的话,美人鱼,听见下雨的声音,说走就走,一点点,前世情人,英雄,不该,土耳其冰淇淋,告白气球,NowYou,爱情废柴'''.split(',')




def genData():

    # clear data
    clear()

    # generating data
    users = [user.objects.create(
        userId=f'user-{i}', name=choice(names), isVip=random() < 0.3) for i in range(USER_NUM)]
    print(users)

    artists = [artist.objects.create(artistId=f'artist-{i}', name=choice(
        names), desc=choice(jokes)) for i in range(ARTIST_NUM)]
    print(artists)

    albums = [album.objects.create(albumId=f'album-{i}', name=choice(
        music_names), desc=choice(jokes)) for i in range(ALBUM_NUM)]

    for al in albums:
        for i in range(randint(1, 4)):
            ar = choice(artists)
            al.artist.add(ar)
        al.save()

    musics = [music.objects.create(musicId=f'music-{i}', name=choice(
        music_names), isVip=random() < 0.4) for i in range(ALBUM_NUM)]

    for m in musics:
        m.album = choice(albums)
        for i in range(randint(1, 2)):
            ar = choice(artists)
            m.artist.add(ar)
        m.save()

    # create group
    groups = {'artist': None, 'user': None}
    permissions = Permission.objects.all()
    for g in groups:
        obj = Group.objects.create(name=g)
        for p in permissions:  # to change
            obj.permissions.add(p)
        obj.save()
        groups[g] = obj

    # create user
    u = User.objects.create_user(
        username='admin', password='music2019', is_staff=True)
    u.groups.add(groups['artist'])
    u.save()
    for m in users:
        u = User.objects.create_user(username=m.userId, password='music2019')
        u.groups.add(groups['user'])
        u.save()

    for m in artists:
        u = User.objects.create_user(username=m.artistId, password='music2019')
        u.groups.add(groups['artist'])
        u.save()


models = [user, artist, album, music, User, Group]


def clear():
    for mdl in models:
        mdl.objects.all().delete()
