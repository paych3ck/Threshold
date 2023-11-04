label threshold_1:
    stop music fadeout 3
    $ renpy.pause(2, hard = True)
    $ persistent.timeofday = "night"
    $ persistent.sprite_time = "night"
    scene bg threshold_ext_tribune_night with Dissolve(2)
    play ambience ambience_camp_center_night fadein 3
    play sound_loop threshold_voices fadein 3
    play music threshold_malachite fadein 3
    threshold_th "Не знаю, зачем я сюда пошел."
    threshold_th "Совсем недавно я просто коротал в отчаянии неделю за неделей, но вот появился непойми кто непойми откуда и сказал, чтобы я {b}обязательно{b} был сегодня здесь."
    threshold_narrator "Он был чуть ли не первым после того глумящегося идиота, кто не был куклой. Да еще так спешил, что даже не обьяснил мне происходящее."
    threshold_narrator "Но даже когда всё рассказал, понятнее эта ситуация не стала."
    threshold_narrator "Возьми что-нибудь защищаться и умри как можно позже."
    threshold_narrator "И всё. {w}Затем он просто растворился в воздухе."
    threshold_narrator "Стоило бы догадаться, что здесь просто будут драки насмерть, но почему-то эта мысль не пришла ко мне в голову."
    threshold_narrator "Прямо сейчас на поле один Пионер с топором догонял трусливо наматывающего круги второго."
    threshold_narrator "Поле представляло собой начерченный по периметру прямоугольник, внутри которого располагалась пара ящиков, мешков и собранной по всему лагерю мебели."
    threshold_narrator "{i}Всё, чтобы разнообразить процесс{/i}, как они говорят."
    threshold_narrator "Зрителей пока что было довольно много. Это те, кто ждет своей очереди. Но с каждым раундом их колличество неизменно падает, пока не останется никого."
    threshold_narrator "Больше всего меня удивляло их отношение ко всему этому всеобщему безумию."
    threshold_narrator "Были те, кому это очевидно нравилось и те, кто чувствовал себя не в своей тарелке. Но пугали меня другие, что безразлично наблюдал, лишь изредка моргая."
    threshold_th "Прямо на их глазах убивают друг друга два их собрата по несчастью, но им абсолютно плевать!"
    threshold_narrator "Я еще раз осмотрел кусок арматуры у меня в руках. {w}Выбрать ничего лучше я не смог. А с ним хоть какой-то опыт был."
    threshold_narrator "Даже эта железная махина не давала мне чувство спокойствия. {w}Один из «участников» убивал особенно быстро, беспощадно и жестоко."
    threshold_narrator "С явным удовольствием он крошил череп проигравшего камнем, пока тело того полностью не растворилось, как при переходе."
    threshold_th "Не знаю, зачем я сюда пошел."
    threshold_narrator "Наматывающий круги трус в конце концов устал и остановился у края поля."
    threshold_th "Кажется, он наконец-то смирился с неизбежным."
    threshold_narrator "В который раз стало не по себе от того, что сейчас произойдет."
    threshold_narrator "Предвкушающий свою победу Пионер с топором только выжидал момента."
    threshold_narrator "Но, когда он почти подошел на расстояние удара, трус просто выпрыгнул за пределы поля!"
    threshold_narrator "«Дровосек» издал нечленораздельный крик и ринулся за беглецом, но, к моему удивлению, пара грозного вида Пионеров быстро остановила его, мгновенно отобрав топор и осадив нерадивого победителя."
    threshold_pi_i_p "Остынь, дуболом. {w}Правила ради тебя не поменяют."
    threshold_narrator "При этом говорящий крепко сжал плечо жертвы рукой. Дровосек с трудом держался, чтобы не закричать от боли."
    threshold_narrator "Беглец в это время, несмотря на презрительные взгляды, с гордым видом занял своё место на пустующей скамье зрителей. {w}Он выглядел чем-то озадаченным, но на этом всё."
    threshold_th "Правила позволяют убежать с поля? {w}Повезло, что я вообще об этом узнал! В случае чего может помочь."
    threshold_narrator "Надежда избежать, казалось, неминуемой смерти, согрела."
    $ renpy.pause(3, hard = True)
    threshold_pi_ann "Три... {w}Два... {w}Начинайте!"
    threshold_narrator "Один за другим проходили и следующие раунды, зрителей оставалось всё меньше."
    threshold_narrator "Пионер сбоку методично записывал результаты в свой дневник. {w}Из того, что говорили рядом, думаю, это будет влиять на конечный номер всех участников. {w}Похоже, и у меня такой будет."
    threshold_th "Но почему никто не отказывается? Почему все продолжают учавствовать? {w}Для них это что, просто соревнование, весёлый конкурс?"
    threshold_th "Здесь собрались одни психи. {w}Они все поголовно сошли с ума."
    threshold_narrator "Кто-то похлопал меня сзади по плечу."
    show threshold_pi normal with dissolve
    threshold_pi_evi "Твой выход, чемпион."
    show threshold_pi smile with dspr
    threshold_narrator "Та тварь, что смеялась над моими потугами найти выход, отвратительно захохотала прямо у моего уха."
    threshold_narrator "Как же мне хотелось сейчас двинуть ему арматурой! "
    threshold_narrator "Если бы не окружающие меня блюстители порядка, я бы так и поступил, но они мне это не простят."
    threshold_narrator "Из-за них же мне придется учавствовать в {w}{i}этом{/i}."
    hide threshold_pi with dissolve
    stop music fadeout 5
    threshold_narrator "Стараясь не показывать своего презрения, я пошел в центр поля."
    scene bg ext_playground_night with dissolve
    threshold_narrator "Пусть до финала не дойду, но, если повезёт, они хотя бы от меня отстанут."
    threshold_narrator "Я занял своё место на поле. {w}Второго пока не было."
    threshold_narrator "И чего он ждет? Неважно, главное не расстеряться. {w}Если держать себя в рука..."
    play music threshold_harbringer fadein 3
    threshold_narrator "Со скамейки встал ОН. {w}ТОТ САМЫЙ ПОМЕШАННЫЙ, РАСКРОШИВШИЙ ДРУГОМУ ЧЕРЕП!"
    threshold_narrator "Мне стало дурно. Я чуть не потерял сознание."
    threshold_th "Почему? {w}ПОЧЕМУ МЕНЯ ПОСТАВИЛИ ПРОТИВ НЕГО!"
    threshold_narrator "Псих неторопливой походкой выходил на поле. В руке у него был только маленький осколок стекла, и всё! Он выходил на противника с арматурой, не имея ничего, кроме обычного осколка!"
    threshold_narrator "Мы пересеклись взглядами. Надо мной будто смеялись, ни во что не ставили."
    threshold_narrator "Когда он почувствовал мой взгляд, то начал беззвучно двигать губами."
    threshold_th "Что он говорит?"
    threshold_pi_mad "Выр{w=1}-ву {w=1}те{w=1}-бе {w=1}ХРЕ{w=1}-БЕТ!"
    play sound threshold_heart
    threshold_narrator "На лбу выступил холодный пот."
    threshold_th "Надо бежать отсюда, плевать на правила, плевать что будет! {w}Надо просто БЕЖАТЬ!"
    threshold_narrator "Но тело не слушалось. {w}Ноги будто примёрзли к месту."
    show threshold_pi smile with dissolve
    threshold_narrator "Псих занял место напротив меня."
    threshold_pi_ann "Три!"
    threshold_narrator "Он больше ничего не говорил. Просто смотрел прямо мне в глаза и скалился."
    threshold_pi_ann "Два!"
    threshold_th "Двигайтесь. {w}ДВИГАЙТЕСЬ!"
    threshold_narrator "Ноги всё еще не слушались меня."
    threshold_pi_ann "Один!"
    threshold_narrator "Я ударил себя кулаком по колену. Боль помогла."
    threshold_pi_ann "Начинаем!"
    scene bg ext_playground_night with dspr:
        zoom 1.05 anchor(48, 27)
        ease 0.15 pos(0, 0)
        ease 0.15 pos(25, 25)
        ease 0.15 pos(0, 0)
        ease 0.15 pos(-25, 25)
        repeat
    play sound_loop threshold_heart
    threshold_narrator "Ведущий не успел договорить, но я уже бросился прочь с поля."
    threshold_narrator "Адреналин стучал в висках и венах, поддерживая мою отчаянную попытку выжить."
    threshold_narrator "За спиной свистел ветер и что-то еще."
    threshold_narrator "Голова болела, но плевать!"
    stop ambience fadeout 2
    stop music fadeout 4
    scene bg ext_beach_night with Dissolve(1)
    play ambience ambience_boat_station_night fadein 2
    threshold_narrator "Я выбежал с поля с такой скоростью, что для остановки понадобилось метров пять. {w}Сердце стучало, как бешенное."
    threshold_narrator "Тот помешанный не стал меня преследовать. {w}Он остановился ровно у черты и следил за мной насмешливым взглядом."
    threshold_narrator "На глаза выступили слезы от радости и облегчения. {w}Жив!"
    threshold_narrator "Мне требовалось передохнуть. Я пошел к ближайшей почти пустой скамейке."
    stop sound_loop fadeout 2
    show threshold_teapot pos2 smile with dissolve
    threshold_pi_teapot "Ну, почти выиграл."    
    threshold_narrator "Это был тот самый парень, что подсказал идею бегства."
    threshold_narrator "Я тихо сел рядом, смахнув каплю с лица."
    threshold_myself "ГАХХ!"
    with flash_red
    threshold_narrator "Мою спину пронзило острой болью."
    threshold_narrator "Я аккуратно, стараясь лишний раз не задеть, провёл по ней рукой."
    threshold_narrator "Спина целиком была располосована. Тонкие ручейки крови текли отовсюду."
    threshold_th "Ну ничего, на следующей неделе пройдёт."
    threshold_narrator "Мне с головой хватало того, что я остался жив."
    threshold_pi_teapot "Ты, наверное, новенький? {w}Как впечатления от первого группового события?"
    threshold_myself "Просто отлично."
    play sound threshold_heart
    threshold_narrator "В голове всё еще звенело."
    threshold_pi_teapot "Тогда поздравляю, ты {b}уже{/b} справился лучше, чем все остальные новоприбывшие."
    threshold_narrator "Он красноречиво посмотрел в сторону пустующих трибун."
    threshold_pi_teapot "Может быть, стоило их ставить друг с другом, а не с машинами массового уничтожения, но что теперь горевать, правда?"
    threshold_myself "Так нас сразу бросили к {b}ним{/b}?! {w}Ты что, больной?!"
    show threshold_teapot pos2 smile:
        xanchor 0.5
        yanchor 0.5
        xalign 0.5
        yalign 0.132
        ease 0.5 zoom 1.232
    threshold_narrator "Воротник его рубашки затрещал в моих руках."
    threshold_pi_teapot "Физически — точно нет."
    hide threshold_teapot
    show threshold_teapot pos2 devil_smile close
    with dspr
    threshold_narrator "Он неуравновешенно рассмеялся."
    threshold_narrator "Ох, если бы только у меня сейчас была в руках арматура! {w}Этот псих просто счастливчик: я выбросил её, чтобы быстрее бежать."
    threshold_th "Нужно остыть. Не сдержусь — стану, как они."
    show threshold_teapot pos2 devil_smile with dspr
    threshold_narrator "Я отпустил его."
    show threshold_teapot pos2 smile2 with dspr
    threshold_pi_teapot "Так просто? И даже истерик не будет?"
    show threshold_teapot pos2 smile3 with dspr
    threshold_pi_teapot "Ну тогда давай заново: зови меня Чайник, а тебя я буду звать так, как захочу."
    threshold_narrator "Чайник протянул мне руку."
    threshold_th "Какое глупое имя."
    threshold_narrator "Мне стало смешно."
    stop ambience fadeout 3
    stop sound_loop fadeout 3
    scene bg black with Dissolve(2)
    $ renpy.pause(2, hard = True)
    jump threshold_2
    
label threshold_2:
    $ persistent.timeofday = "day"
    $ persistent.sprite_time = "day"
    $ renpy.pause(2, hard = True)
    scene bg ext_island_day with Dissolve(2)
    play music threshold_new_years_end fadein 5
    play ambience ambience_lake_shore_day fadein 2
    threshold_narrator "Я уже третий час смотрел за неподвижным поплавком на воде."
    threshold_myself "Эй, Чайник, ты уверен, что здесь вообще есть рыба?"
    show threshold_teapot pos2 smile3 with dissolve
    threshold_teapot "Есть. {w}Одна-единственная, но есть!"
    threshold_th "С другой стороны, ровная водная гладь успокаивала. {w}Насколько долго можно смотреть на воду?"
    threshold_narrator "В отличие от меня, держащего подобие удочки в руках, Чайник закрепил свое с помощью бревна и просто валялся на траве, сложив руки за шеей."
    threshold_teapot "Точно, всё время с тех пор забывал!"
    threshold_narrator "Воскликнул он."
    threshold_narrator "Затем достал из одного кармана листок бумаги, пробитый нитью, а с другой — обычный фломастер."
    threshold_narrator "И быстро начал что-то рисовать."
    threshold_teapot "Вот! Носи это с честью."
    threshold_narrator "Он протянул мне результат своей работы, на котором кривыми буквами было написано:"
    show threshold_note with dissolve
    threshold_narrator "бЕг уКреПляЕт зДоРоВьЕ."
    threshold_myself "Ээээ... {w}Спасибо. {w}Наверное."
    threshold_narrator "С Чайником мы сошлись на удивление быстро. Да, он был полностью невменяем, но в хорошем смысле."
    threshold_narrator "Он был невероятно талантлив, мог сделать всё, что угодно. Главной преградой для него была только собственная рассеяность."
    threshold_narrator "На тот турнир он собрал бомбу, способную вынести железную дверь. Она обеспечила ошеломительную победу в первом раунде, вот только была «бомбочка» только одна."
    threshold_narrator "Чайник мог занять первое место. А так - конец списка, ненамного выше меня."
    hide threshold_note with dissolve
    threshold_narrator "Я осторожно привязал подарок к грудному карману."
    threshold_narrator "Очень повезло, что удалось уйти от того ненормального, победившего в конце концов всех и каждого."
    threshold_narrator "Даже подготовленные участники никакой угрозы ему не представляли. Разве что финал был более-менее равным."
    threshold_myself "Раз ты уже поднял эту тему, то чья была идея так подставить новичков?"
    threshold_teapot "Так говоришь... Вот мы все сидели и думали: как бы вам жизнь подпортить!"
    threshold_teapot "Остынь, горячая голова. {w}Это было просто совпадением. Вас было не так много. А строить специально щадящую турнирную таблицу — много чести."
    threshold_teapot "Здесь не курорт, по крайней мере не полностью. Подстраиваться и беречь вас - ни в чьих интересах."
    threshold_teapot "Тем более так у вас был шанс проявить себя. Мы-вот, например, сошлись."
    threshold_teapot "А вообще следи за поплавком. Если рыба уйдёт, я тебя за ней брошу. Будешь вплавь догонять."
    threshold_myself "Ладно, ладно. {w}Чайник? Я еще кое-что спросить хотел..."
    threshold_teapot "Ну валяй."
    threshold_myself "Эти голоса в шахтах, кому они принадлежат?"
    show threshold_teapot pos2 sad with dspr
    threshold_narrator "Он секунду промолчал. {w}Потом занял сидячее положение и внимательно посмотрел мне в глаза."
    threshold_teapot "Слушай, а ты часом не в бункере живешь?"
    threshold_myself "Нет... {w}Почему ты спрашиваешь?"
    threshold_teapot "Да так. Примета есть такая — перед тем, как двинуть кукухой, ребятки начинают жить в бункере."
    play sound sfx_bush_leaves 
    $ renpy.pause(2, hard = True)
    show threshold_teapot pos2 smile3:
        linear 1 xalign 0.2
    $ renpy.pause(1, hard = True)
    show threshold_nit bulging3_l at right with dspr
    threshold_narrator "Наш разговор прервало появление нового Пионера."
    threshold_narrator "Я сразу напрягся и замолчал."
    threshold_narrator "Практически от них всех стоит ждать беды. Мне уже хватило общения и с тем, который доставал меня в моём лагере."   
    threshold_teapot "О, заходи, гостем будешь!"
    threshold_narrator "Чайник гостеприимно подвинулся."
    threshold_guest "Приветствую брата по несчастью."
    threshold_narrator "Я аккуратно поворачивался, чтобы в случае чего, успеть сорваться с места, но, похоже, гость это заметил."
    threshold_narrator "Ограничусь пока тем, что буду держать его в поле зрения."
    threshold_narrator "Он аккуратно кивнул головой, отдавая вежливый поклон."
    threshold_teapot "Ты пришел к нам или от кого бежишь?"
    threshold_guest "Снова устроили потасовку в общем лагере. {w}Не хотел принимать участие."
    threshold_narrator "Новоприбывший сел на песке, сложив ноги."
    threshold_teapot "Кто с кем?"
    threshold_guest "Община первосменников опять на что-то обиделась. Думал, они собьются в группу медленнее. У вас ушло смен двадцать."
    threshold_narrator "Не слышал об этой «общине». Может, прибился бы к ним, если бы не Чайник."
    threshold_teapot "У {b}нас{/b} ушло. Тем более, я послушал..."
    threshold_narrator "Чайник бросил взгляд в мою сторону. {w}От внимания гостя стало неуютно."
    threshold_teapot "И у них есть общий враг. Так что не переживай по этому поводу."
    threshold_teapot "Почему наш новоиспечённый чемпион не усмирил волнения?"
    threshold_guest "Пока его не трогать, то он — просто божий одуванчик. К счастью, обеим сторонам ума хватает."
    threshold_guest "А вы чем занимаетесь?"
    threshold_teapot "Рыбу ловим."
    threshold_guest "Рыбу? Могу простить новичку, но ты-то, Чайник."
    threshold_teapot "Послушай, здесь есть рыба, ладно? Я не сошел с ума."
    threshold_teapot "На неделе до турнира мне пришлось выбросить ботинок из лодки(не спрашивай почему), и, когда пришлось его забирать, мою обувь кто-то утащил на метров двадцать от точки погружения."
    threshold_guest "Правда?"
    threshold_narrator "Гость выглядел явно не впечатлённым."
    threshold_guest "И в какой день это чудо произошло?"
    threshold_teapot "В первый, но это прямо вообще не важно."
    threshold_guest "Я бы так не сказал. {w}Ты ведь знаешь, есть одно примечательное ракообразное, что ловит младшая на пляже..."
    threshold_narrator "Брови Чайника медленно поползли вверх."
    show threshold_nit bulging3_l_smile at right with dspr
    threshold_teapot "Хочешь сказать, что... {w}Да иди ты к черту!"
    play sound sfx_water_splash    
    threshold_narrator "В порыве он схватил свою самодельную удочку и запустил её метров на сорок в озеро."
    threshold_narrator "Гость просто наслаждался каждой эмоцией Чайника."
    threshold_teapot "Блин, вот надо было тебе... {w}Да я мог бы смен семьдесят тут рыбачить в счастливом неведении, в упорных поисках той самой рыбины! Но тут пришел ты, и все мои мечты с надеждами — в трубу."
    threshold_teapot "К черту иди!"
    threshold_narrator "Докинул он в ответ на неуёмный смех собеседника."
    threshold_teapot "Вот это..."
    threshold_narrator "Теперь Чайник обращался уже ко мне."
    threshold_teapot "Суть моей жизни здесь. {w}Концентрированная, в бутылочке."
    threshold_narrator "Я отвернулся к поплавку, пряча прыснувшую улыбку."
    stop ambience fadeout 3
    stop music fadeout 3
    scene bg black with Dissolve(2)
    $ renpy.pause(2, hard = True)
    jump threshold_3

label threshold_3:
    $ persistent.timeofday = "sunset"
    $ persistent.sprite_time = "sunset"
    $ renpy.pause(2, hard = True)
    scene bg ext_road_sunset with Dissolve(2)
    play music threshold_death_note fadein 10
    play ambience ambience_ext_road_evening fadein 3
    threshold_narrator "В тот день Чайник предпринял что-то достаточно глупое, чтобы ожидать это от него, но в то же время неординарное настолько, что я всё равно оказался удивлён."
    threshold_myself "Как? Как ты вообще её сюда дотащил?"
    threshold_narrator "Мой полный удивления взгляд был полностью прикован к стоящей прямо на остановке Волге."
    show threshold_teapot pos1 devil_smile with dissolve
    threshold_teapot "Ну, знаешь... {w}Ма-а-а-а-агия..."
    threshold_teapot "Могу потом как-нибудь научить, если будет настроение и мне это не наскучит."
    threshold_myself "Не научишь?"
    threshold_teapot "Ха-ха. {w}Не-а!"
    hide threshold_teapot with dissolve
    threshold_narrator "Чайник залез в машину, усевшись за рулем."
    threshold_narrator "Затем, вспомнив, что он не один, волшебник перебросил через бардачок ногу и пинком открыл дверь со стороны пассажира."
    threshold_teapot "Падай."
    threshold_narrator "Мне оставалось только пожать плечами."
    scene bg threshold_volga_cg with dissolve
    threshold_th "Только сейчас я понял, что никогда толком и не замечал Волгу. Она была больше неподвижным элементом декора. Такое себе дерево, на которое не обращаешь внимания."
    threshold_narrator "Но вот Чайник, видит сквозь все эти условности и ограничения. {w}Странный он."
    threshold_narrator "Всё это время он, кстати, просто стучал пальцами по баранке, никак не трогая коробку передач или вообще хоть что-то."
    threshold_myself "Эй?"
    threshold_narrator "Я аккуратно окликнул его."
    threshold_teapot "Чего?"
    threshold_myself "Ты будешь заводить её?"
    threshold_teapot "Заводить? {w}Зачем?"
    threshold_narrator "Весь его вид излучал непонимание моего вопроса."
    threshold_teapot "Не знаю, как ты, но я просижу здесь до конца смены, любуясь закатом."
    threshold_narrator "Выучив со временем его повадки, с уверенностью могу сказать только что он может как шутить, так и говорить это на полном серьёзе."
    threshold_narrator "Мне даже сложно предположить, как он будет себя вести, если сойдет с ума. {w}Наверное, точно так же."
    threshold_narrator "Похоже, моя озадаченность отразилась и на лице, потому что Чайник решил добавить."
    threshold_teapot "Угу, сейчас заведу. Но с одним условием."
    threshold_myself "Что такое?"
    threshold_narrator "Не нравится мне, когда он так говорит."
    threshold_teapot "Скажи: Дыр-дыр-дыр."
    threshold_th "Что?"
    threshold_myself "Что?"
    threshold_teapot "Ну-же, давай, это просто. Дыр-дыр-дыр!"
    
    menu:
        "Дыр-дыр-дыр":
            threshold_narrator "Сокрушенный вздох."
            threshold_myself "Дыр-дыр-дыр."
            threshold_th "Чувствую себя идиотом."
            threshold_narrator "Он повернулся ко мне."
            threshold_teapot "Это что сейчас было? {w}Где запал, где эмоции?!"
            threshold_myself "Ты серьёзно?"
            threshold_teapot "Давай!"
            threshold_myself "Дыр-дыр-дыр!"
            threshold_teapot "Сильнее!"
            threshold_myself "ДЫР-ДЫР-ДЫР!"
            threshold_teapot "Даааааааа..."
            threshold_narrator "Чайник расслабленно откинулся, насколько это позволяло сиденье Волги."
            threshold_narrator "В следующий раз делай так сразу."
            jump threshold_end_f
            
        "Промолчать":
            pass
    
    threshold_narrator "Отчасти от нежелания, отчасти от неожиданности, но я промолчал."
    threshold_teapot "Не расслышал? {w}Глухомань!"
    threshold_teapot "Дыр-дыр-дыр, говорю, скажи!"
    threshold_teapot "Хм, это была тавтология или мне показалось?"
    threshold_narrator "Проворчал он сам себе."
    
    menu:
        "Дыр-дыр-дыр":
            threshold_narrator "Ну что же, мне не жалко, пусть порадуется."
            threshold_myself "Дыр-дыр-дыр."
            threshold_teapot "Вот, видишь? Капля терпения и моей доброты открывает все двери."
            jump threshold_end_f
            
        "Промолчать":
            pass
            
    threshold_narrator "От меня всё еще не было ни звука."
    threshold_teapot "Нет, ну в этот раз ты точно слышал. {w}Наверное."
    threshold_teapot "Чего же ты... {w}Ааааа, понял!"
    threshold_teapot "Ты хочешь устроить дуэль терпения!"
    threshold_teapot "Не хотел бы тебя огорчать, но ты не с тем связался, сынок. Я выучил наизусть «Две тактики социал-демократии в демократической революции» и не побоюсь ими воспользоваться."
    threshold_teapot "А твои эти выпады — так, на один зубок."
    $ renpy.pause(1, hard = True)
    threshold_teapot "Ты лучше сдайся по-хорошему, а то же я их вслух зачитывать буду."
    
    menu:
        "Дыр-дыр-дыр":
            threshold_narrator "Я посмотрел на него и наконец решился."
            threshold_myself "Дыр-дыр-дыр."
            threshold_teapot "Хе-хе-хе, знал, что это сработает."
            threshold_teapot "Не волнуйся, многие пали перед безжалостным натиском «Двух тактик»."
            threshold_teapot "Тот парень с рыбалки, например, от этого литературного шедевра в моём исполнении вообще истерику схватил..."
            threshold_teapot "Ну да я как-то отхожу от темы."
            play sound_loop sfx_bus_interior_moving fadein 2
            threshold_teapot "Эээх, если у вас плохое настроение, то мы едем к вам!"
            threshold_narrator "Он азартно завёл машину и, крутанув руль, дал резвый старт."
            threshold_narrator "Я прислонился лбом к стеклу своего окна."      
            jump threshold_end_f_2

        "Промолчать":
            pass
    
    threshold_narrator "..."
    threshold_teapot "Ну, парень, я тебя предупреждал по хорошему."
    threshold_teapot "Ты сам навлёк на себя это."
    threshold_narrator "Сделав вдох на все свои лёгкие, Чайник нарочито скучным голосом начал."
    $ threshold_set_mode_nvl()
    threshold_teapot "{i} В революционный момент очень трудно поспеть за событиями, которые дают поразительно много нового материала к оценке тактических лозунгов революционных партий. Настоящая брошюра писана до одесских событий. Мы уже указали в «Пролетарии», что эти события заставили даже тех социал-демократов, которые создали теорию восстания процесса и отрицали пропаганду временного революционного правительства, перейти или начать переходить фактически на сторону своих оппонентов. {/i}"
    $ threshold_set_mode_adv()
    threshold_narrator "После окончания абзаца Чайник остановился, чтобы перевести дыхание и дать мне шанс избежать продолжения этого литературного вечера."
    
    menu:
        "Дыр-дыр-дыр":
            threshold_teapot "Ну, ты выдержал больше, чем три четверти населения лагерей."
            threshold_teapot "Гордись собой."
            threshold_teapot "Знаешь, делай так чаще, мне даже понравилось. {w}Я, как истинный рыцарь, своей смекалкой и упорством завалил вредного дракона!"
            play sound_loop sfx_bus_interior_moving fadein 2
            threshold_narrator "Закончив самовосхваление, Чайник, сияя от радости, завёл наконец машину."
            jump threshold_end_f_2
            
        "Промолчать":
            pass
            
    threshold_narrator "Пауза, устроенная им, затянулась."
    threshold_narrator "На мне застыл искренне удивлённый взгляд."
    threshold_narrator "Он, похоже, не верил, что кто-то осознанно мог обречь себя на такую судьбу."
    threshold_narrator "Прошелся по мне взглядом в последний раз."
    threshold_narrator "Я всё еще молчал."
    threshold_teapot "Знаешь, за свою жизнь здесь я многое понял. {w}Вечность слишком коротка, чтобы тратить её на таких, как ты."
    threshold_teapot "А еще, уверен, что тебе уже говорил это, но иди к черту."
    threshold_narrator "Он всё еще бормотал себе что-то под нос, когда машина сдвинулась."
    threshold_th "Хорошо, что Чайник быстро отходит."
    scene bg threshold_ext_power_line_sunset at threshold_bus_moving with dissolve
    threshold_narrator "Я уставился на вид за окном."
    threshold_th "Может, жизнь здесь не так уж и плоха?"
    threshold_th "Да, это не то, о чём я мечтал, но и в той жизни всё хорошо бы не сложилось."
    threshold_th "Так или иначе, суть вещей и тут, и там одна и та же."
    threshold_th "Стоит провести несколько смен подальше ото всех. Хорошо всё обдумать."
    threshold_narrator "Тихое закатное солнце усыпляло."
    threshold_narrator "Навалилось странное желание просто отдохнуть. От всех мыслей, тревог и надежд."
    threshold_narrator "Я сладко зевнул."
    threshold_th "Что же, остаётся только ждать, что нам принесёт завтрашний день."
    stop ambience fadeout 3
    scene bg black with Dissolve(2)
    stop music fadeout 4
    $ renpy.pause(2, hard = True)
    jump threshold_true_end
    
label threshold_end_f:    
    play sound_loop sfx_bus_interior_moving fadein 2
    "Добившись желаемого, Чайник с довольным видом завёл машину."
    
label threshold_end_f_2:
    scene bg threshold_ext_power_line_sunset at threshold_bus_moving with dissolve
    threshold_narrator "Я смотрел в своё окно."
    threshold_narrator "Ощущения были очень похожи на автобус. Но разницы как раз хватало, чтобы новизна бодрила и не навивала вечную тоску."
    threshold_narrator "По ту сторону стекла пролетал знакомый пейзаж."
    threshold_th "Зачем я здесь? Как я сюда попал? Почему не один?"
    threshold_th "Сколько я задаю себе вопросов..."
    threshold_th "Может, давно стоило смириться с неизвестностью? С их устоем?"
    threshold_th "В конце концов, быть шестерёнкой в системе не так и сложно."
    threshold_th "Когда-то, если повезёт, найду своё место."
    threshold_th "Или сойду с ума. Тогда забот уж точно станет меньше."
    threshold_narrator "Но вдруг когда-то я смогу выбраться?"
    threshold_narrator "Главное — не опускать рук?"
    threshold_narrator "Тихое закатное солнце умиротворяло."
    threshold_narrator "Я посмотрел на водителя."
    threshold_narrator "Чайник кайфовал от момента не меньше меня."
    threshold_narrator "Ну, всё будет как будет. {w}Хорошо или плохо."
    threshold_narrator "Машина тихо ехала по бесконечной дороге."
    stop ambience fadeout 3
    stop sound_loop fadeout 3
    scene bg black with Dissolve(2)
    stop music fadeout 4
    $ renpy.pause(2, hard = True)
    return
    
label threshold_true_end:
    $ persistent.timeofday = "day"
    $ persistent.sprite_time = "day"
    $ renpy.pause(2, hard = True)
    scene bg int_musclub_day
    show threshold_nit normal_l
    with Dissolve(2)
    play ambience ambience_music_club_day fadein 3
    threshold_teapot "И потом он заснул. {w}А еще позже начал храпеть."
    threshold_teapot "Прикинь!"
    threshold_narrator "В порыве эмоций я вдарил столовой ложкой у меня в руках по барабану."
    threshold_narrator "Ниточник как-то моего возмущения не разделял."
    threshold_teapot "Да ты хоть вкурсе, насколько было сложно вытащить ту железяку на остановку? Я себе спину чуть не надорвал."
    threshold_teapot "Подай мне вон ту гитару, кстати."
    threshold_nit "Разве тебе нужно еще больше струн?"
    threshold_teapot "Струн очень много не бывает! Еще лагеря два обойти нужно."
    threshold_nit "Так что случилось с тем парнем? Чем он занимается сейчас?"
    threshold_narrator "Я смотал очередную нить с гитары."
    threshold_th "А эти штуковины вообще выдержат мой запуск в небо?"
    threshold_teapot "В жизни не поверишь. Забрался в шахты."
    threshold_nit "Ты его предупреждал, нет?"
    threshold_teapot "Да, {w}да! {w}Но кто ж меня когда слушает? {w}Если бы все делали как я советую, везде бы царил мир!"
    threshold_nit "Навещаешь его?"
    threshold_teapot "Нет. Вдруг, это заразно? Может, тот парнишка связался с плохой компанией и теперь заслуженно горюет у разбитого бункера?"
    threshold_th "Есть вообще заразный синдром отшельника? {w}Ух, давно уже медэнциклопедию не перечитывал..."
    threshold_narrator "Мне еще куча ткани понадобится, а то воздушный змей меня не поднимет."
    threshold_teapot "Давай, пошевеливайся, солнце еще в зените."
    threshold_narrator "Смотав струны в моток и забросив его в забитую доверху сумку, я полез в следующий разлом."
    stop ambience fadeout 3
    play sound threshold_portal_use
    scene bg black with flash
    $ renpy.pause(2, hard = True)

    return