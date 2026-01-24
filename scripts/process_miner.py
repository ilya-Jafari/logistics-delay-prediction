import pandas as pd
import pm4py
from pm4py.objects.log.util import dataframe_utils
from pm4py.objects.conversion.log import converter as log_converter

# ۱. شبیه‌سازی داده‌های فرآیندی (Event Log)
# در دنیای واقعی این دیتا از سیستم ERP یا GPS استخراج می‌شود
data = {
    'case_id': ['B1', 'B1', 'B1', 'B2', 'B2', 'B3', 'B3', 'B3', 'B3'],
    'activity': ['Order Received', 'Customs Check', 'Delivered', 
                 'Order Received', 'Delivered',
                 'Order Received', 'Customs Check', 'Warehouse Hold', 'Delivered'],
    'timestamp': pd.to_datetime(['2026-01-01', '2026-01-02', '2026-01-05',
                                 '2026-01-01', '2026-01-03',
                                 '2026-01-01', '2026-01-02', '2026-01-06', '2026-01-10'])
}

df = pd.DataFrame(data)

# ۲. آماده‌سازی برای PM4PY
df = dataframe_utils.convert_timestamp_columns_in_df(df)
df = df.rename(columns={'case_id': 'case:concept:name', 'activity': 'concept:name', 'timestamp': 'time:timestamp'})

# ۳. استخراج نقشه فرآیند (Process Discovery)
log = log_converter.apply(df)
dfg, start_activities, end_activities = pm4py.discover_directly_follows_graph(log)

# ۴. نمایش بصری (خروجی این دستور یک نقشه گرافیکی است)
pm4py.view_dfg(dfg, start_activities, end_activities)

print("✅ Process Map generated. Look for bottlenecks in 'Customs Check' or 'Warehouse Hold'.")