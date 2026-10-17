# Python Learning Roadmap 2026

**Цель:** Переход с Junior на Middle Python Developer.
**Стек:** Python 3.12+, FastAPI, PostgreSQL, Docker, Poetry, Pytest.

## Текущий статус
- [x] Месяц 1: Базовые инструменты и синтаксис
- [ ] Месяц 2: Инженерная культура
- [ ] Месяц 3: Production-ready сервисы

## Месяц 1: Декораторы, магические методы и алгоритмы

### Неделя 1: Декораторы 📅 (13.10 – 19.10)
**Книга:** Python Tricks (главы про декораторы)
- [ ] Прочитать теорию
- [ ] Написать `@timer` ([код](src/month_1/week_1_decorators/timer.py))
- [ ] Написать `@retry` 
- [ ] Написать `@singleton`

### Неделя 2: Магические методы 📅 (20.10 – 26.10)
**Книга:** Fluent Python
- [ ] Класс `Vector` с `__add__`, `__mul__`
- [ ] Дескриптор `LazyProperty`
- [ ] Контекстный менеджер `Timer`

### Неделя 3: Алгоритмы (LeetCode) 📅 (27.10 – 02.11)
- [ ] 15 задач Easy
- [ ] 5 задач Medium
- [ ] Two Sum ([решение](src/month_1/week_3_algorithms/two_sum.py))

## Правила коммитов
Используем Conventional Commits для чистой истории:
* `feat:` — новая функция (например, `feat: add @retry decorator`)
* `fix:` — исправление ошибки
* `docs:` — обновление документации
* `refactor:` — изменение кода без смены логики
