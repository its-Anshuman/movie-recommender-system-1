mkdir -p ~/.streamlit/

echo "\
[server]\n\
port = $PORT\n\
enableCORS = false\n\
headless = true\n\
\n\
" > ~/.streamlit/config.toml

wget --no-check-certificate "https://drive.google.com/uc?export=download&id=1chG_WEVVkWRI5Iv8bsVn7og-WnK-1MiS" -O similarity.pkl
