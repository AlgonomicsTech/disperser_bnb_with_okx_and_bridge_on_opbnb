#  Algonomics - disperser_bnb_with_okx_and_bridge_on_opbnb


## 🔗 Links

🔔 CHANNEL: [AlgonomicTech](https://t.me/AlgonomicsTech)

💬 CHAT: [Join the Chat](https://t.me/+7zMjbT6mRBZlMGEy)

💰 DONATION EVM ADDRESS: 0x4A080654795e526801954493BD0D712609d0ccEF



## 🤖 | Функционал:

🟢 Отправка указаного в настройках количества BNB c биржи [OKX](https://www.okx.com/ru) 

🟢 Перевод BNB c BSC в OpBNB






## 🚀 Installation
```
pip install -r requirements.txt

# Перед началом работы в главной дериктории проекта проекта сосдаем папку data, в данной папке создаем файли address.txt и private_keys.txt.

# Команда для запуска

 python main.py   

```

## ⚙️ Config

| Name | Description                                                                                                             |
| --- |-------------------------------------------------------------------------------------------------------------------------|
| address.txt | Адреса для вывода bnb, каждый с новой строки.                                                                           |
| private_keys.txt | Приватные ключи где уже есть bnb, для вывода в орbnb, каждый с новой строки.                                            |
|config.py| Для вывода с OKX, обязательно заполняєм OKX_API_KEY, OKX_SECRET_KEY и OKX_PASSPHRASE, остальные параметры - по желанию! |


## ⚡️Инстукция

🟢 Перед первым выводом средств с биржи, нужно добавить адреса в белый список, можно добавлять максимум 20 адресов за один подход

🟢 Также если еще нет, создаем API ключи і пассфразу

🟢 Заполняєм файлы и настройки

🟢 Запускаем python main.py  

🟢 Если средства уже на кошельках, виполняєм сразу шаг два, если нет, сделайте паузу в 5 мин. при переходе на второй этап.

🟢 Важно при повторной работе с кошельками очищать файлы success_send.txt и success_bridge.txt, также в этих файлах можно смотреть прогрес работы.



## Дисклеймер (Предупреждение)

Важно:
- При использовании данного программного обеспечения избегайте использования аккаунтов, где хранятся личные средства. Не инвестируйте больше, чем вы готовы потерять.
- Разработчики этого приложения не несут ответственности за ваши финансовые потери. Пользователи должны самостоятельно оценивать все риски и проводить собственные исследования перед осуществлением финансовых операций.
- Этот дисклеймер не является юридической консультацией. При необходимости обратитесь к квалифицированному специалисту.
