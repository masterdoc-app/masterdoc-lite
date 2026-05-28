#!/usr/bin/env python3
"""Adapt flosync Mary page → Masterdoc RU landing."""
from pathlib import Path

p = Path(__file__).with_name("index.html")
html = p.read_text(encoding="utf-8")

# Brand / CSS class
html = html.replace("Machine Mary", "Masterdoc")
html = html.replace("Machine ", "master")
html = html.replace('<span class="machine">master</span><span class="mary">Mary</span>', '<span class="machine">master</span><span class="mary">doc</span>')
html = html.replace('<span class="machine">master</span><span class="mary">doc</span>', '<span class="machine">master</span><span class="mary">doc</span>')
html = html.replace("em.mary", "em.doc")
html = html.replace('class="mary"', 'class="doc"')
html = html.replace("Mary", "Masterdoc")
html = html.replace("Masterdoc ·", "Masterdoc ·")  # noop

# Fix over-replacements in URLs/emails
html = html.replace("Masterdoc operator app", "Masterdoc operator app")
html = html.replace("pushkar@flosync.io", "mail@antonbutov.com")
html = html.replace("aniket@flosync.io", "mail@antonbutov.com")

pairs = [
    ('lang="en"', 'lang="ru"'),
    ("AI troubleshooting copilot for the shop floor", "ИИ-копилот для поиска неисправностей в цеху"),
    ("AI Troubleshooting Copilot for the Shop Floor", "ИИ-копилот для поиска неисправностей в цеху"),
    ("Your operators handle <em class=\"doc\">zero</em><br />on their own.", "Операторы сами не справляются ни с <em class=\"doc\">одним</em><br />из них."),
    ("downtime events a&nbsp;month.", "случаев простоя в&nbsp;месяц."),
    ('<span class="stat">25</span>', '<span class="stat">25</span>'),
    (
        "Masterdoc guides operators through troubleshooting — step by step, grounded in <b>your machines</b> and <b>your fault history</b>. Every event becomes a record. Knowledge compounds. It doesn't retire, forget, or vary by shift.",
        "Masterdoc ведёт операторов через поиск и устранение неисправностей — шаг за шагом, на основе <b>вашего оборудования</b> и <b>истории сбоев</b>. Каждое событие становится записью. Знания накапливаются. Они не уходят на пенсию, не забываются и не зависят от смены.",
    ),
    ("Currently piloting with leading auto-component manufacturers.", "Пилот с производителями промышленного оборудования и сетей эксплуатации."),
    ("Book a 30-min demo", "Демо"),
    ("See how it works", "Как это работает"),
    ("How it works", "Как это работает"),
    ("The numbers", "Цифры"),
    ("Team", "Команда"),
    ("Book a demo", "Демо"),
    ("Book a Demo", "Демо"),
    ('aria-label="Masterdoc home"', 'aria-label="Masterdoc — главная"'),
    ("Live · 02:14 AM", "В эфире · 02:14"),
    ("Voice or text input", "Голос или текст"),
    ("FOUND", "НАЙДЕНО"),
    ("Voice · Active", "Голос · активен"),
    ("Hey. What's going on with Station 12?", "Привет. Что со станцией 12?"),
    ("weird clicking, and the feed jammed twice in the last hour", "странные щелчки, подача дважды заклинивала за час"),
    ("Listening · noise-cancel on", "Слушаю · шумоподавление"),
    ("Transcribing…", "Распознаю…"),
    ("Tap to describe what's happening", "Опишите, что происходит"),
    ("Voice", "Голос"),
    ("getting error 14 on the screen", "на экране ошибка 14"),
    (
        "Error 14 is usually a sensor timeout on the feed assembly. Let's narrow it down — try one:",
        "Ошибка 14 обычно — таймаут датчика узла подачи. Сузим круг — попробуйте:",
    ),
    ("82% confidence · 11 similar", "◉ 82% уверенность · 11 похожих"),
    ("Fault record", "Запись о сбое"),
    ("◆ Saved to library", "◆ Сохранено в базу"),
    ("Cleared a <b>feed jam</b> caused by a worn feed guide.", "Устранили <b>заклинивание подачи</b> из‑за изношенного направляющего."),
    ("Station", "Станция"),
    ("Line", "Линия"),
    ("Resolved", "Решено"),
    ("Heard", "Сообщили"),
    ("Did", "Сделали"),
    ("Cause", "Причина"),
    ("Next", "Далее"),
    ("Clicking noise, two jams in one hour", "Щелчки, два заклина за час"),
    ("Cleared the chute and re-seated the roller", "Прочистили желоб, установили ролик"),
    ('<em>"Feed guide is worn, flag for maintenance."</em>', '<em>«Направляющая изношена — отметить на ТО».</em>'),
    ("Replace guide at next shift change", "Заменить направляющую при смене смены"),
    ("Saved · no escalation", "Сохранено · без эскалации"),
    ("Share", "Поделиться"),
    ("Done", "Готово"),
    ("Scan", "Скан"),
    ("Describe", "Описание"),
    ("Guide", "Подсказки"),
    ("Resolved", "Готово"),
    ("<b>Tap a step</b> to flip through the prototype", "<b>Нажмите шаг</b>, чтобы листать прототип"),
    ("Before vs. After · same machine, two shifts", "До и после · одна машина, две смены"),
    ("Two shifts. Same machine. <em class=\"doc\">One has Masterdoc.</em>", "Две смены. Одна машина. <em class=\"doc\">С Masterdoc.</em>"),
    (
        "The dramatic save matters. The routine save matters more — that's where the volume lives.",
        "Яркий спасённый ремонт важен. Рутинная экономия времени важнее — там и лежит объём.",
    ),
    ("Before", "До"),
    ("After", "После"),
    ("Without", "Без"),
    ("With", "С"),
    ("Without Masterdoc", "Без Masterdoc"),
    ("With Masterdoc", "С Masterdoc"),
    ("The <span class=\"time\">2&nbsp;AM</span> phone call.", "Звонок в <span class=\"time\">2&nbsp;ночи</span>."),
    (
        "Operator hears an unusual noise from Station&nbsp;12. Tries restarting — no luck. Line leader takes a look — not sure either. They <b>call maintenance at home</b>. Tech drives in, asks \"what happened?\" Operator re-explains. Tech re-diagnoses from scratch, finds a material jam in the feed assembly. Clears it in 3 minutes.",
        "Оператор слышит шум на станции&nbsp;12. Перезапуск не помогает. Сменный мастер тоже не уверен. <b>Звонят механику домой</b>. Тот приезжает, переспрашивает. Диагностирует с нуля, находит заклинивание в узле подачи. Устраняет за 3 минуты.",
    ),
    ("Downtime · cumulative", "Простой · нарастающий"),
    ("min · no record", "мин · без записи"),
    ("No phone call. <span class=\"time\">7&nbsp;minutes.</span>", "Без звонка. <span class=\"time\">7&nbsp;минут.</span>"),
    (
        "Operator opens Masterdoc, taps Station&nbsp;12, records: <em>\"weird noise, machine stopped.\"</em> Masterdoc matches the pattern — two options: <b>(A)</b> check feed assembly for jam, <b>(B)</b> check drive belt tension. Operator taps&nbsp;A, clears the jam, line restarts.",
        "Оператор открывает Masterdoc, выбирает станцию&nbsp;12: <em>«странный шум, станок встал»</em>. Masterdoc предлагает варианты: <b>(А)</b> проверить заклинивание подачи, <b>(Б)</b> натяжение привода. Оператор выбирает&nbsp;А, линия запускается.",
    ),
    ("min · fault logged", "мин · сбой записан"),
    ("The error code <span class=\"time\">nobody remembers.</span>", "Код ошибки, который <span class=\"time\">никто не помнит.</span>"),
    (
        "Operator sees an error code on the HMI. Not sure what it means. Asks around — nobody's sure. Calls maintenance. <b>25 minutes pass.</b> Tech comes, hits a reset sequence nobody on the line knew about. Same error Thursday. Same delay.",
        "На HMI код ошибки. Никто не уверен. Зовут механиков. <b>25 минут простоя.</b> Механик делает сброс, о котором линия не знала. В четверг — та же история.",
    ),
    ("min · for a 2-min fix", "мин · при 2‑минутном ремонте"),
    ("Knowledge that <span class=\"time\">compounds.</span>", "Знания, которые <span class=\"time\">накапливаются.</span>"),
    (
        "\"Getting error&nbsp;14.\" Masterdoc: <em>\"Sensor timeout. (A) Reset — hold START 3&nbsp;sec then CLEAR, (B) Check proximity sensor on left rail.\"</em> Operator taps&nbsp;A. Machine runs. Thursday, a different operator gets Error&nbsp;14. <b>Masterdoc already knows.</b>",
        "«Ошибка&nbsp;14». Masterdoc: <em>«Таймаут датчика. (А) Сброс — START 3&nbsp;сек, затем CLEAR, (Б) датчик слева на рельсе»</em>. Оператор жмёт&nbsp;А. В четверг другой оператор снова видит 14 — <b>Masterdoc уже знает.</b>",
    ),
    ("min · added to knowledge base", "мин · в базу знаний"),
    (
        "These routine events happen <b>3&ndash;4× per week</b> at a typical plant. Each one costs 20&ndash;45 minutes while the escalation chain runs. That's <b>8&ndash;12 hours of lost production a month</b> — on problems that should've taken five minutes.",
        "Такие рутинные сбои — <b>3–4 раза в неделю</b> на типичном заводе. Каждый съедает 20–45 минут, пока идёт эскалация. Это <b>8–12 часов потерянного выпуска в месяц</b> — на задачи, которые должны занимать пять минут.",
    ),
    ("No separate documentation step. <b>The interaction IS the record.</b>", "Отдельный шаг документирования не нужен. <b>Сам диалог — это запись.</b>"),
    ("Masterdoc works across your floor", "Masterdoc на всём вашем цехе"),
    ("Any machine with a control panel. No sensors. No hardware. No IT project.", "Любой станок с панелью управления. Без датчиков. Без железа. Без IT‑проекта."),
    ("Four steps. <em class=\"doc\">Five</em> seconds to scan.", "Четыре шага. <em class=\"doc\">Пять</em> секунд на скан."),
    ("QR code on the machine. Phone in the operator's pocket. No new dashboards, no training program, no IT project.", "QR на станке. Телефон в кармане оператора. Без новых дашбордов, программ обучения и IT‑проектов."),
    ("01 / Trigger", "01 / Старт"),
    ("Machine acts up.", "Станок ведёт себя странно."),
    ("Alarm, unusual noise, bad parts, an unexpected stop.", "Авария, шум, брак, неожиданная остановка."),
    ("02 / Open", "02 / Открыть"),
    ("Operator opens Masterdoc.", "Оператор открывает Masterdoc."),
    ("QR scan or dropdown. Describe the problem by voice or text.", "QR или список. Описание голосом или текстом."),
    ("03 / Guide", "03 / Подсказка"),
    ("Masterdoc guides.", "Masterdoc ведёт."),
    ("Tappable A/B/C options. Right things tried in the right order.", "Варианты А/Б/В. Правильные действия в правильном порядке."),
    ("04 / Resolve", "04 / Итог"),
    ("Resolved or escalated.", "Решено или эскалация."),
    ("Fixed → logged. Not fixed → maintenance gets the full context.", "Починили → записали. Нет → механикам весь контекст."),
    ("Why this is a <em class=\"doc\">$50&nbsp;billion</em> problem.", "Почему это проблема на <em class=\"doc\">$50&nbsp;млрд</em>."),
    ("The math behind the problem.", "Математика проблемы."),
    ("Problem scale", "Масштаб"),
    ("downtime events per plant, per month", "событий простоя на завод в месяц"),
    ("Knowledge crisis", "Кадры"),
    ("US manufacturing workers retiring by 2033", "рабочих уходят на пенсию к 2033 (США)"),
    ("Cost", "Стоимость"),
    ("lost annually to unplanned downtime in US manufacturing", "потерь в год из‑за внеплановых простоев (США)"),
    ("Masterdoc's ROI", "Окупаемость"),
    ("return on every dollar spent on Masterdoc", "возврат на каждый вложенный доллар"),
    ("Who's behind this", "Кто мы"),
    ("Built by the team behind <em>200K+ industrial IoT</em> deployments.", "Команда с опытом <em>цифровизации эксплуатации</em> и промышленных внедрений."),
    ("Common questions", "Вопросы"),
    ("What people ask <em class=\"doc\">before</em> the first call.", "Что спрашивают <em class=\"doc\">до</em> первого звонка."),
    ("What happens when Masterdoc can't fix it?", "Что если Masterdoc не решит проблему?"),
    (
        "She escalates — but with context, not chaos. Maintenance gets a package: what the operator described, every step already attempted, photos from the session, and Masterdoc's narrowed diagnosis. They start from a specific problem, not square one. And when they fix it, that resolution feeds back into Masterdoc — so next time, the operator handles it alone.",
        "Эскалация — с контекстом, не хаосом. Механики получают: описание оператора, все попытки, фото, суженный диагноз. Не с нуля. Исправление попадает в базу — в следующий раз оператор справится сам.",
    ),
    ("Do we need to install sensors or hardware?", "Нужны ли датчики или оборудование?"),
    (
        "No. Masterdoc works with your existing machines and your operators' phones. QR code on the machine, web app on the phone. No sensors, no edge devices, no IT project. No app store download — works in any phone browser.",
        "Нет. Работает со станками как есть и с телефонами операторов. QR на станке, веб в браузере. Без датчиков, edge и IT‑проекта. Без установки из магазина приложений.",
    ),
    ("How does Masterdoc know our machines?", "Откуда Masterdoc знает наши станки?"),
    (
        "We start by loading 10–15 fault patterns per machine — curated from your manuals, your maintenance logs, and interviews with your best technicians. From day one of the pilot, every real event adds to the library. In three months, Masterdoc knows patterns that aren't in any manual.",
        "Старт: 10–15 типовых сбоев на станок — из паспортов, журналов и интервью с лучшими механиками. С первого дня пилота каждое событие пополняет базу. Через три месяца — паттерны, которых нет в инструкциях.",
    ),
    ("How is Masterdoc different from general AI tools?", "Чем Masterdoc отличается от обычного ИИ?"),
    (
        "ChatGPT doesn't know that Station 12's feed assembly jammed three times last month. It can't escalate to your maintenance team with context. It doesn't learn from your specific events. Masterdoc is grounded in your machines, your history, your plant. Generic AI gives generic answers.",
        "ChatGPT не знает, что узел подачи станции 12 заклинивал трижды за месяц. Не эскалирует механикам с контекстом. Masterdoc опирается на ваши станки, историю и цех.",
    ),
    ("What does the pilot look like?", "Как выглядит пилот?"),
    (
        "One machine, three weeks. We build the fault library from your actual machines and your team's knowledge. You see real events flowing through Masterdoc within the first week. At the end: a clear picture of resolution rates, time saved, and knowledge captured. Then you decide.",
        "Один станок, три недели. Библиотека сбоев из ваших машин и знаний команды. Реальные события в Masterdoc уже на первой неделе. В конце — цифры по времени, решениям и накопленным знаниям.",
    ),
    ("Book a call", "Запись на демо"),
    ("See <em>Masterdoc</em> in action.", "Посмотрите <em>Masterdoc</em> в деле."),
    (
        "<b>30 minutes.</b> We'll show you Masterdoc on a real machine, walk through how it fits your plant, and answer questions. No pitch deck.",
        "<b>30 минут.</b> Покажем Masterdoc на реальном оборудовании, обсудим внедрение на вашем объекте. Без презентации.",
    ),
    (
        "<b>Bring</b><span>One downtime story from your plant. We'll show you exactly how Masterdoc would handle it.</span>",
        "<b>Принесите</b><span>Один реальный простой с вашего объекта — покажем, как Masterdoc его разберёт.</span>",
    ),
    (
        "<b>Walk away with</b><span>A clear picture of where Masterdoc fits, ROI math for your plant, and pilot terms if it's a fit.</span>",
        "<b>Уйдёте с</b><span>Пониманием, где Masterdoc встраивается, расчётом окупаемости и условиями пилота.</span>",
    ),
    ("Prefer email? ", "Предпочитаете email? "),
    ("Pick a time · 30-min slot · Pacific / Eastern", "Оставьте заявку · 30 минут"),
    ("Loading available times…", "Загрузка…"),
    ("Built by ", "Продукт "),
    ("Flosync ↗", "Masterdoc"),
    ("© 2026 Flosync, Inc.", "© 2026 Masterdoc"),
]

for old, new in pairs:
    html = html.replace(old, new)

# Remove hero stats (user request)
import re
html = re.sub(
    r'\s*<div class="hero-meta">.*?</div>\s*',
    "\n",
    html,
    count=1,
    flags=re.DOTALL,
)

# Replace team / founders with Masterdoc contact
founders_block = """    <div class="founders">
      <div class="founder">
        <div class="role">Основатель</div>
        <div class="name">Бутов Антон</div>
        <div class="bio">
          Masterdoc — электронные журналы эксплуатации, заявки на ремонт и документация у агрегата. Фокус: сети объектов с холодильным и торговым оборудованием, уход от Excel без тяжёлого 1С.
        </div>
        <div class="links">
          <a href="#book">Записаться на демо</a>
          <a href="mailto:mail@antonbutov.com">mail@antonbutov.com</a>
        </div>
      </div>
    </div>"""

html = re.sub(
    r'<div class="founders">.*?</div>\s*<div class="pilot-line">',
    founders_block + '\n\n    <div class="pilot-line">',
    html,
    count=1,
    flags=re.DOTALL,
)

# Replace Calendly with contact form
form_block = """    <div class="cal-frame" id="calFrame">
      <div class="cal-frame-head">Заявка на демо · ответим в течение рабочего дня</div>
      <div class="cal-body" style="padding:24px;background:var(--s1);border:1px solid var(--bd)">
        <form class="contact-form" action="https://formspree.io/f/maqvkbob" method="POST" style="display:flex;flex-direction:column;gap:14px">
          <input type="hidden" name="_subject" value="Masterdoc lite: заявка с лендинга">
          <label style="display:flex;flex-direction:column;gap:6px;font-size:13px;font-weight:500">
            Имя *
            <input type="text" name="name" required style="padding:12px;border:1px solid var(--bd2);background:var(--bg);font:inherit">
          </label>
          <label style="display:flex;flex-direction:column;gap:6px;font-size:13px;font-weight:500">
            Email *
            <input type="email" name="email" required style="padding:12px;border:1px solid var(--bd2);background:var(--bg);font:inherit">
          </label>
          <label style="display:flex;flex-direction:column;gap:6px;font-size:13px;font-weight:500">
            Телефон
            <input type="tel" name="phone" style="padding:12px;border:1px solid var(--bd2);background:var(--bg);font:inherit">
          </label>
          <label style="display:flex;flex-direction:column;gap:6px;font-size:13px;font-weight:500">
            Сообщение
            <textarea name="message" rows="4" style="padding:12px;border:1px solid var(--bd2);background:var(--bg);font:inherit;resize:vertical"></textarea>
          </label>
          <button type="submit" class="btn" style="justify-content:center;margin-top:8px"><span>Отправить</span><span class="arr">→</span></button>
        </form>
      </div>
    </div>"""

html = re.sub(
    r'<div class="cal-frame" id="calFrame">.*?</div>\s*</div>\s*</section>',
    form_block + "\n  </div>\n</section>",
    html,
    count=1,
    flags=re.DOTALL,
)

# Machine types marquee — Russian samples
machine_ru = [
    "Холодильные витрины", "Компрессорные агрегаты", "HVAC", "Торговое оборудование",
    "Линии розлива", "Упаковочные линии", "Прессы", "ЧПУ", "Сварка", "Конвейеры",
]
marquee_inner = "".join(f'<span class="mi">{m}</span>' for m in machine_ru * 2)
html = re.sub(
    r'<div class="marquee-inner">\s*<span class="mi">Stamping Presses</span>.*?</div>\s*</div>\s*<!-- Row 2',
    f'<div class="marquee-inner">{marquee_inner}</div>\n    </div>\n\n    <!-- Row 2',
    html,
    count=1,
    flags=re.DOTALL,
)

brands_ru = ["Atlant", "Bitzer", "Danfoss", "Copeland", "Embraco", "GEA", "Carrier", "Daikin", "Mitsubishi", "Siemens"]
brands_inner = "".join(f'<span class="mi">{b}</span>' for b in brands_ru * 2)
html = re.sub(
    r'<div class="marquee-inner right">\s*<span class="mi">Fanuc</span>.*?</div>',
    f'<div class="marquee-inner right">{brands_inner}</div>',
    html,
    count=1,
    flags=re.DOTALL,
)

html = html.replace(
    "<title>Masterdoc — AI troubleshooting copilot for the shop floor</title>",
    "<title>Masterdoc — ИИ-копилот для эксплуатации оборудования</title>",
)
html = html.replace(
    'content="Masterdoc guides machine operators',
    'content="Masterdoc ведёт операторов',
)

p.write_text(html, encoding="utf-8")
print("OK", len(html))
