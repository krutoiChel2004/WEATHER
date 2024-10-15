# Базовый образ для Node.js
FROM node:18-alpine AS build

# Установка рабочей директории
WORKDIR /app

# Копируем package.json и package-lock.json для установки зависимостей
COPY package*.json ./

# Установка зависимостей
RUN npm install

# Копируем все файлы приложения
COPY . .

# Билдим приложение для продакшена
RUN npm run build

# Запуск веб-сервера на базе Nginx для обслуживая билдов
FROM nginx:alpine AS production

# Копируем собранные файлы в Nginx
COPY --from=build /app/dist /usr/share/nginx/html

# Копируем конфигурацию Nginx (если она есть)
# COPY nginx.conf /etc/nginx/nginx.conf

# Открываем порт 80
EXPOSE 80

# Запуск Nginx
CMD ["nginx", "-g", "daemon off;"]
