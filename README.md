# Домашнее задание «Регулярные выражения»

Доброго дня и заранее спасибо!

P.S. попытался сделать максимально близко к пройденым темам, по предложенной логике, без классов и итераторов. 
Столкнулся с проблемой обработки ФИО. Иногда перенос происходил с потерей отчества (беда от join, split)
Удалять лишние пробелы черевато, попытался сделать более-менее универсальное правило по которому будет 
идти заполнение: первое именованное поле и будет фамилией.

Иных идей на момент выполнения в голову не пришло. С одной стороны это не лучший вариант, а с другой 
если пользователь будет вносить данные полностью неверно (и в графу имени писать все одной строкой),
либо хаотично заполнять строки - придется прикручивать анализатор текста.

Но и в этом случае существует немало фамилий, которые будут неотличимы и для человека от имени или отчества,
перевода иностранных и пр. Например, даже корректная запись: Султан (имя), Антон (!фамилия!) Михайлович (отчество)
или Султановна (фамилия) Альбина (имя) Султановна (фамилия) станет той еще проблемой... 
Подскажите, как с таким справляются (не учитвая принудительный инструктаж пользователей)?
