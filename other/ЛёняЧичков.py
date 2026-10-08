import pandas as pd
import re
import os
import time
print(os.getcwd())

INPUT_FILE = "Копия Опись склад 7147 (эксперимент).xlsx"
OUTPUT_FILE = "Опись_склад_7147_с_остаточной_стоимостью.xlsx"
NOT_FOUND_FILE = "не_сопоставлено.xlsx"

def norm_sn(x):
    """Нормализация серийного номера: строка, верхний регистр, без пробелов и дефисов."""
    if pd.isna(x):
        return ""
    s = str(x).strip().upper()
    s = re.sub(r"[\s\-_/]+", "", s)
    # отсекаем мусор
    if s in ("", "N/A", "#N/A", "ОТСУТСТВУЕТ", "НЕ ЧИТАЕТСЯ", "Б/Н", "-"):
        return ""
    return s

# --- Читаем листы ---
df1 = pd.read_excel(INPUT_FILE, sheet_name="Серийные номера")
df2 = pd.read_excel(INPUT_FILE, sheet_name="Идентифицировано")


print(f"Лист 1 (Серийные номера): {len(df1)} строк")
print(f"Лист 2 (Идентифицировано): {len(df2)} строк")

# --- Нормализуем SN ---
df1["_sn"] = df1["Серийный номер"].apply(norm_sn)
df2["_sn"] = df2["Заводской номер"].apply(norm_sn)

# --- Справочник: SN -> остаточная стоимость (берём максимальную при дублях) ---
ref = (df2[df2["_sn"] != ""]
       .groupby("_sn", as_index=False)["Остаточная стоимость"]
       .max())

print(f"Уникальных SN в листе 2: {len(ref)}")

# --- Сопоставление ---
df1 = df1.merge(ref, on="_sn", how="left", suffixes=("", "_из_листа2"))

# Если в листе 1 уже была колонка "Остаточная стоимость" — заполняем её
if "Остаточная стоимость_из_листа2" in df1.columns:
    df1["Остаточная стоимость"] = df1["Остаточная стоимость_из_листа2"]
    df1.drop(columns=["Остаточная стоимость_из_листа2"], inplace=True)

# --- Статистика ---
matched = df1["Остаточная стоимость"].notna().sum()
print(f"Сопоставлено: {matched} из {len(df1)}")
print(f"Не найдено: {len(df1) - matched}")

# --- Сохраняем результат ---
df1.drop(columns=["_sn"], errors="ignore").to_excel(OUTPUT_FILE, index=False)

# --- Отдельно — что не сопоставилось ---
not_found = df1[df1["Остаточная стоимость"].isna()].copy()
not_found.drop(columns=["_sn"], errors="ignore").to_excel(NOT_FOUND_FILE, index=False)

print(f"\nГотово:\n  {OUTPUT_FILE}\n  {NOT_FOUND_FILE}")