
from pathlib import Path

import joblib
import pandas as pd
import streamlit as st


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="C",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# ============================================================
# PROFESSIONAL UI
# ============================================================

st.markdown(
    """
    <style>
    :root {
        --primary: #315efb;
        --ink: #182230;
        --muted: #667085;
        --line: #e6e9ee;
        --canvas: #f7f8fa;
    }

    .stApp {
        background: var(--canvas);
        color: var(--ink);
    }

    [data-testid="stHeader"] {
        background: transparent;
    }

    [data-testid="stSidebar"] {
        display: none;
    }

    .block-container {
        max-width: 1180px;
        padding-top: 1.5rem;
        padding-bottom: 3rem;
    }

    .brand {
        font-size: 1.5rem;
        font-weight: 800;
        letter-spacing: -0.7px;
        color: var(--ink);
    }

    .brand-subtitle {
        color: var(--muted);
        font-size: 0.85rem;
        margin-top: 2px;
        margin-bottom: 1.2rem;
    }

    .page-title {
        font-size: 2.25rem;
        font-weight: 800;
        letter-spacing: -1.1px;
        line-height: 1.2;
        color: var(--ink);
        margin-top: 1.1rem;
    }

    .page-description {
        color: var(--muted);
        font-size: 1rem;
        line-height: 1.7;
        margin-top: 0.5rem;
        margin-bottom: 1.4rem;
        max-width: 760px;
    }

    .section-title {
        font-size: 1.2rem;
        font-weight: 750;
        color: var(--ink);
        margin-top: 0.6rem;
        margin-bottom: 0.25rem;
    }

    .section-description {
        color: var(--muted);
        font-size: 0.88rem;
        margin-bottom: 1rem;
    }

    .panel {
        background: white;
        border: 1px solid var(--line);
        border-radius: 12px;
        padding: 1.15rem;
        margin: 0.3rem 0;
    }

    .result-card {
        background: white;
        border: 1px solid var(--line);
        border-radius: 14px;
        padding: 1.4rem;
        margin-top: 1rem;
    }

    .result-label {
        font-size: 0.8rem;
        text-transform: uppercase;
        font-weight: 750;
        letter-spacing: 0.07em;
        margin-bottom: 0.6rem;
    }

    .result-number {
        font-size: 2.2rem;
        font-weight: 800;
        letter-spacing: -1px;
        color: var(--ink);
    }

    .result-description {
        color: var(--muted);
        line-height: 1.7;
        margin-top: 0.5rem;
    }

    .footer {
        border-top: 1px solid var(--line);
        margin-top: 2.5rem;
        padding-top: 1rem;
        color: #7a8493;
        font-size: 0.78rem;
        line-height: 1.7;
    }

    div[data-testid="stMetric"] {
        background: white;
        border: 1px solid var(--line);
        border-radius: 10px;
        padding: 0.9rem;
    }

    div[data-testid="stMetricLabel"] {
        color: var(--muted);
    }

    div[data-testid="stMetricValue"] {
        color: var(--ink);
        font-weight: 750;
    }

    /* Form & Section Headings */
    div[data-testid="stForm"] {
        background: #ffffff !important;
        border: 1px solid var(--line);
        border-radius: 14px;
        padding: 1.3rem;
        color: #000000 !important;
    }

    div[data-testid="stForm"] h4 {
        color: #000000 !important;
        font-weight: 800 !important;
        margin-top: 0.2rem !important;
        margin-bottom: 0.75rem !important;
    }

    /* Labels for All Inputs in Form & Sample Selector */
    div[data-testid="stForm"] label,
    div[data-testid="stForm"] label p,
    div[data-testid="stForm"] label span,
    div[data-testid="stForm"] label div,
    div[data-testid="stSelectbox"] label,
    div[data-testid="stSelectbox"] label p {
        color: #000000 !important;
        font-weight: 600 !important;
        font-size: 0.92rem !important;
    }

    /* Selectbox Boxes & Selected Option Text */
    div[data-baseweb="select"] > div {
        background-color: #ffffff !important;
        border: 1.5px solid #cbd5e1 !important;
        border-radius: 8px !important;
    }

    div[data-baseweb="select"] * {
        color: #000000 !important;
        font-weight: 600 !important;
    }

    div[data-baseweb="select"] svg {
        fill: #000000 !important;
        color: #000000 !important;
    }

    /* Dropdown Popover / Option List When Opened */
    div[data-baseweb="popover"],
    ul[data-baseweb="menu"],
    div[data-baseweb="menu"] {
        background-color: #ffffff !important;
        border: 1px solid #cbd5e1 !important;
        border-radius: 8px !important;
    }

    ul[data-baseweb="menu"] li,
    ul[data-baseweb="menu"] li * {
        color: #000000 !important;
        font-weight: 600 !important;
    }

    ul[data-baseweb="menu"] li:hover,
    ul[data-baseweb="menu"] li[aria-selected="true"] {
        background-color: #f1f5f9 !important;
    }

    /* Number Inputs */
    div[data-testid="stNumberInput"] input {
        color: #000000 !important;
        background-color: #ffffff !important;
        border: 1.5px solid #cbd5e1 !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
    }

    div[data-testid="stNumberInput"] button {
        background-color: #f8fafc !important;
        border-color: #cbd5e1 !important;
    }

    div[data-testid="stNumberInput"] button * {
        color: #000000 !important;
    }

    /* Slider Text */
    div[data-testid="stSlider"] * {
        color: #000000 !important;
    }

    /* Form Descriptions & Captions */
    div[data-testid="stForm"] .stCaption,
    div[data-testid="stForm"] p {
        color: #475467 !important;
    }

    div[data-testid="stFormSubmitButton"] button {
        min-height: 2.8rem;
        font-weight: 700;
        border-radius: 8px;
    }

    div[data-testid="stFormSubmitButton"] button[kind="primary"] {
        background: var(--primary);
        border-color: var(--primary);
        color: #ffffff !important;
    }

    div[data-testid="stFormSubmitButton"] button[kind="primary"] * {
        color: #ffffff !important;
    }

    div[data-testid="stFormSubmitButton"] button[kind="primary"]:hover {
        background: #2449d8;
        border-color: #2449d8;
    }

    div[data-testid="stRadio"] > label {
        display: none;
    }

    div[data-testid="stRadio"] div[role="radiogroup"] {
        gap: 0.65rem;
        border-bottom: 2px solid #e2e8f0;
        padding-bottom: 1rem;
        margin-bottom: 0.5rem;
    }

    div[data-testid="stRadio"] div[role="radiogroup"] label {
        background: #ffffff !important;
        border: 2px solid #0f172a !important;
        border-radius: 9px;
        padding: 0.5rem 1.25rem;
        cursor: pointer;
        transition: all 0.15s ease;
    }

    div[data-testid="stRadio"] div[role="radiogroup"] label * {
        color: #000000 !important;
        font-weight: 700 !important;
        font-size: 0.92rem !important;
    }

    div[data-testid="stRadio"] div[role="radiogroup"] label:hover {
        background: #f1f5f9 !important;
    }

    div[data-testid="stRadio"] div[role="radiogroup"] label:has(input:checked) {
        background: #0f172a !important;
        border-color: #0f172a !important;
    }

    div[data-testid="stRadio"] div[role="radiogroup"] label:has(input:checked) * {
        color: #ffffff !important;
        font-weight: 800 !important;
    }

    hr {
        border-color: var(--line);
    }

    @media (max-width: 700px) {
        .block-container {
            padding-top: 1rem;
        }

        .page-title {
            font-size: 1.8rem;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# MODEL ARTIFACTS
# ============================================================

@st.cache_resource(show_spinner="Loading prediction model...")
def load_artifacts():
    current_dir = Path(__file__).resolve().parent

    candidates = [
        current_dir / "models",
        current_dir.parent / "models",
    ]

    models_dir = next(
        (path for path in candidates if path.is_dir()),
        candidates[0],
    )

    paths = {
        "model": models_dir / "churn_model.pkl",
        "scaler": models_dir / "scaler.pkl",
        "columns": models_dir / "training_columns.pkl",
    }

    missing = [
        path.name
        for path in paths.values()
        if not path.is_file()
    ]

    if missing:
        return None, None, None, (
            f"Missing model files in {models_dir}: "
            + ", ".join(missing)
        )

    try:
        model = joblib.load(paths["model"])
        scaler = joblib.load(paths["scaler"])
        columns = list(joblib.load(paths["columns"]))

        return model, scaler, columns, None

    except Exception as exc:
        return None, None, None, str(exc)


model, scaler, training_columns, load_error = load_artifacts()


# ============================================================
# SAMPLE CUSTOMER PROFILES
# ============================================================

PRESETS = {
    "Custom customer": {
        "gender": "Male",
        "senior": "No",
        "partner": "No",
        "dependents": "No",
        "tenure": 12,
        "phone": "Yes",
        "lines": "No",
        "internet": "DSL",
        "security": "No",
        "backup": "Yes",
        "device": "No",
        "support": "No",
        "tv": "No",
        "movies": "No",
        "contract": "Month-to-month",
        "paperless": "Yes",
        "payment": "Electronic check",
        "monthly": 70.0,
        "total": 840.0,
    },

    "Short-tenure example": {
        "gender": "Female",
        "senior": "No",
        "partner": "No",
        "dependents": "No",
        "tenure": 2,
        "phone": "Yes",
        "lines": "No",
        "internet": "Fiber optic",
        "security": "No",
        "backup": "No",
        "device": "No",
        "support": "No",
        "tv": "Yes",
        "movies": "Yes",
        "contract": "Month-to-month",
        "paperless": "Yes",
        "payment": "Electronic check",
        "monthly": 89.5,
        "total": 179.0,
    },

    "Long-tenure example": {
        "gender": "Male",
        "senior": "No",
        "partner": "Yes",
        "dependents": "Yes",
        "tenure": 64,
        "phone": "Yes",
        "lines": "Yes",
        "internet": "DSL",
        "security": "Yes",
        "backup": "Yes",
        "device": "Yes",
        "support": "Yes",
        "tv": "No",
        "movies": "No",
        "contract": "Two year",
        "paperless": "No",
        "payment": "Bank transfer (automatic)",
        "monthly": 55.2,
        "total": 3532.8,
    },
}


FIELD_KEYS = list(PRESETS["Custom customer"].keys())


def apply_preset():
    """Update all form values when a sample profile is selected."""
    preset = PRESETS[st.session_state.profile]

    for field in FIELD_KEYS:
        st.session_state[field] = preset[field]


for field, value in PRESETS["Custom customer"].items():
    if field not in st.session_state:
        st.session_state[field] = value

if "profile" not in st.session_state:
    st.session_state.profile = "Custom customer"


# ============================================================
# TOP HEADER (CHURN LOGO & DESCRIPTION UP)
# ============================================================

st.markdown(
    """
    <div style="display:flex; align-items:center; gap:0.75rem; margin-top:0.3rem; margin-bottom:0.4rem;">
        <div style="width:40px; height:40px; border-radius:10px; background:#182230; color:#ffffff; display:flex; align-items:center; justify-content:center; font-size:1.25rem; font-weight:800;">C</div>
        <div class="page-title" style="margin:0; font-size:2.2rem;">Customer Churn Prediction</div>
    </div>
    <div class="page-description">
        Estimate the likelihood of a telecom customer leaving. Enter their account details to generate a prediction using the trained machine learning model.
    </div>
    """,
    unsafe_allow_html=True,
)

# ============================================================
# CUSTOMER INSIGHTS NAVIGATION (DOWN)
# ============================================================

st.markdown(
    """
    <div class="brand" style="margin-top:0.6rem; margin-bottom:0.15rem;">Customer Insights</div>
    <div class="brand-subtitle" style="margin-bottom:0.75rem;">
        Customer analytics and churn prediction workspace
    </div>
    """,
    unsafe_allow_html=True,
)

page = st.radio(
    "Navigation",
    ["Predict Churn", "Dataset Insights", "About"],
    horizontal=True,
    label_visibility="collapsed",
    key="main_navigation",
)

st.write("")


# ============================================================
# DATASET LOADER
# ============================================================

@st.cache_data(show_spinner="Loading customer dataset...")
def load_customer_dataset():
    current_dir = Path(__file__).resolve().parent

    candidates = [
        current_dir / "data" / "telco_customer_churn.csv",
        current_dir / "telco_customer_churn.csv",
        current_dir.parent / "data" / "telco_customer_churn.csv",
        current_dir / "data" / "WA_Fn-UseC_-Telco-Customer-Churn.csv",
        current_dir / "WA_Fn-UseC_-Telco-Customer-Churn.csv",
        current_dir / "data" / "telco_customer_churn.txt",
    ]

    data_path = next(
        (path for path in candidates if path.is_file()),
        None,
    )

    if data_path is None:
        return None, None, (
            "Dataset not found. Add your CSV to the data folder "
            "as telco_customer_churn.csv."
        )

    try:
        data = pd.read_csv(data_path)

        required = {
            "Churn",
            "Contract",
            "InternetService",
            "PaymentMethod",
            "tenure",
            "MonthlyCharges",
            "TotalCharges",
        }

        missing = required.difference(data.columns)

        if missing:
            return None, data_path, (
                "Missing dataset columns: "
                + ", ".join(sorted(missing))
            )

        data["TotalCharges_numeric"] = pd.to_numeric(
            data["TotalCharges"],
            errors="coerce",
        )

        return data, data_path, None

    except Exception as exc:
        return None, data_path, str(exc)


# ============================================================
# PAGE 1: PREDICT CHURN
# ============================================================

if page == "Predict Churn":



    if load_error:
        st.error("The prediction model could not be loaded.")
        st.code(load_error)
        st.info(
            "Place churn_model.pkl, scaler.pkl and "
            "training_columns.pkl inside your models folder."
        )
        st.stop()

    st.markdown(
        '<div class="section-title">Customer details</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="section-description">
            Choose a sample profile or enter your own customer data.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.selectbox(
        "Sample customer",
        list(PRESETS.keys()),
        key="profile",
        on_change=apply_preset,
        help="You can edit any field after selecting a profile.",
    )

    with st.form("customer_form", clear_on_submit=False):

        personal_col, service_col, billing_col = st.columns(
            3,
            gap="large",
        )

        with personal_col:
            st.markdown("#### Personal & account")

            gender = st.selectbox(
                "Gender",
                ["Male", "Female"],
                key="gender",
            )

            senior = st.selectbox(
                "Senior citizen",
                ["No", "Yes"],
                key="senior",
            )

            partner = st.selectbox(
                "Has a partner",
                ["Yes", "No"],
                key="partner",
            )

            dependents = st.selectbox(
                "Has dependents",
                ["Yes", "No"],
                key="dependents",
            )

            tenure = st.slider(
                "Customer tenure (months)",
                min_value=0,
                max_value=72,
                key="tenure",
            )

            contract = st.selectbox(
                "Contract",
                ["Month-to-month", "One year", "Two year"],
                key="contract",
            )

        with service_col:
            st.markdown("#### Subscribed services")

            internet = st.selectbox(
                "Internet service",
                ["DSL", "Fiber optic", "No"],
                key="internet",
            )

            phone = st.selectbox(
                "Phone service",
                ["Yes", "No"],
                key="phone",
            )

            line_options = (
                ["Yes", "No"]
                if phone == "Yes"
                else ["No phone service"]
            )

            if st.session_state.lines not in line_options:
                st.session_state.lines = line_options[0]

            lines = st.selectbox(
                "Multiple lines",
                line_options,
                key="lines",
            )

            addon_options = (
                ["Yes", "No"]
                if internet != "No"
                else ["No internet service"]
            )

            addon_fields = [
                ("Online security", "security"),
                ("Online backup", "backup"),
                ("Device protection", "device"),
                ("Tech support", "support"),
                ("Streaming TV", "tv"),
                ("Streaming movies", "movies"),
            ]

            addon_values = {}

            for label, key in addon_fields:
                if st.session_state[key] not in addon_options:
                    st.session_state[key] = addon_options[0]

                addon_values[key] = st.selectbox(
                    label,
                    addon_options,
                    key=key,
                )

        with billing_col:
            st.markdown("#### Billing & payment")

            paperless = st.selectbox(
                "Paperless billing",
                ["Yes", "No"],
                key="paperless",
            )

            payment = st.selectbox(
                "Payment method",
                [
                    "Electronic check",
                    "Mailed check",
                    "Bank transfer (automatic)",
                    "Credit card (automatic)",
                ],
                key="payment",
            )

            monthly = st.number_input(
                "Monthly charges ($)",
                min_value=0.0,
                max_value=120.0,
                step=1.0,
                key="monthly",
            )

            total = st.number_input(
                "Total charges ($)",
                min_value=0.0,
                max_value=100000.0,
                step=10.0,
                key="total",
            )

            st.caption(
                f"Tenure × monthly charges: "
                f"${tenure * monthly:,.2f}"
            )

        st.write("")

        submitted = st.form_submit_button(
            "Run churn prediction",
            type="primary",
            use_container_width=True,
        )

    # --------------------------------------------------------
    # MODEL PREDICTION
    # --------------------------------------------------------

    if submitted:

        input_dict = {
            "gender": gender,
            "SeniorCitizen": 1 if senior == "Yes" else 0,
            "Partner": partner,
            "Dependents": dependents,
            "tenure": tenure,
            "PhoneService": phone,
            "MultipleLines": lines,
            "InternetService": internet,
            "OnlineSecurity": addon_values["security"],
            "OnlineBackup": addon_values["backup"],
            "DeviceProtection": addon_values["device"],
            "TechSupport": addon_values["support"],
            "StreamingTV": addon_values["tv"],
            "StreamingMovies": addon_values["movies"],
            "Contract": contract,
            "PaperlessBilling": paperless,
            "PaymentMethod": payment,
            "MonthlyCharges": float(monthly),
            "TotalCharges": float(total),
        }

        try:
            raw_df = pd.DataFrame([input_dict])

            encoded_df = pd.get_dummies(raw_df)

            aligned_df = encoded_df.reindex(
                columns=training_columns,
                fill_value=0,
            )

            scaled_input = scaler.transform(aligned_df)

            prediction = int(model.predict(scaled_input)[0])

            probability = float(
                model.predict_proba(scaled_input)[0][1]
            )

            probability = min(max(probability, 0.0), 1.0)

            st.session_state.last_result = {
                "input": input_dict,
                "prediction": prediction,
                "probability": probability,
            }

        except Exception as exc:
            st.error(f"Prediction failed: {exc}")
            st.info(
                "Ensure the model, scaler and training columns "
                "were saved from the same training pipeline."
            )

    # --------------------------------------------------------
    # DISPLAY PREDICTION RESULT
    # --------------------------------------------------------

    result = st.session_state.get("last_result")

    if result:

        probability = result["probability"]
        prediction = result["prediction"]
        percentage = probability * 100

        if probability >= 0.60:
            risk_name = "Higher risk"
            risk_color = "#b42318"
            background = "#fff0ee"

            summary = (
                "This customer has an elevated estimated likelihood "
                "of leaving. Review service quality, billing concerns "
                "and contract suitability."
            )

            actions = [
                "Review recent service and support issues.",
                "Check whether the current plan meets customer needs.",
                "Consider a suitable retention offer when justified.",
            ]

        elif probability >= 0.40:
            risk_name = "Moderate risk"
            risk_color = "#9a6700"
            background = "#fff6df"

            summary = (
                "The estimated churn probability is in the moderate "
                "range. Review customer feedback and monitor "
                "potential warning signs."
            )

            actions = [
                "Review customer satisfaction and billing clarity.",
                "Check recent support interactions.",
                "Monitor the account for additional warning signs.",
            ]

        else:
            risk_name = "Lower risk"
            risk_color = "#18794e"
            background = "#eaf7ef"

            summary = (
                "This profile has a lower estimated likelihood of "
                "churn. Continue providing reliable service and "
                "maintain regular customer communication."
            )

            actions = [
                "Maintain reliable service and communication.",
                "Continue routine customer satisfaction checks.",
                "Avoid unnecessary retention discounts.",
            ]

        st.divider()

        st.markdown(
            '<div class="section-title">Prediction result</div>',
            unsafe_allow_html=True,
        )

        st.markdown(
            f"""
            <div class="result-card"
                 style="border-left: 4px solid {risk_color};">
                <div class="result-label"
                     style="color: {risk_color};">
                    {risk_name}
                </div>
                <div class="result-number">
                    {percentage:.1f}%
                </div>
                <div class="result-description">
                    Estimated probability of customer churn.
                    {summary}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.write("")

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Model prediction",
            "Churn" if prediction == 1 else "No churn",
        )

        col2.metric(
            "Churn probability",
            f"{percentage:.1f}%",
        )

        col3.metric(
            "Risk category",
            risk_name,
        )

        st.markdown("#### Suggested next steps")

        for action in actions:
            st.markdown(f"- {action}")

        st.progress(
            probability,
            text=f"Estimated churn probability: {percentage:.1f}%",
        )

        st.caption(
            "The probability is a model estimate, not a guarantee. "
            "Risk categories use this app's presentation thresholds "
            "and are not universal business standards."
        )


# ============================================================
# PAGE 2: DATASET INSIGHTS
# ============================================================

elif page == "Dataset Insights":

    st.markdown(
        '<div class="page-title">Dataset insights</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="page-description">
            Explore customer churn patterns, contract types,
            internet services and payment methods in the
            telecom dataset.
        </div>
        """,
        unsafe_allow_html=True,
    )

    customer_data, dataset_path, dataset_error = (
        load_customer_dataset()
    )

    if dataset_error:
        st.warning(dataset_error)

    else:
        churn_flag = (
            customer_data["Churn"]
            .astype(str)
            .str.strip()
            .str.lower()
            .eq("yes")
        )

        stay_flag = (
            customer_data["Churn"]
            .astype(str)
            .str.strip()
            .str.lower()
            .eq("no")
        )

        total_customers = len(customer_data)
        churned_count = int(churn_flag.sum())
        retained_count = int(stay_flag.sum())

        churn_rate = (
            churned_count / total_customers * 100
            if total_customers else 0
        )

        retained_rate = (
            retained_count / total_customers * 100
            if total_customers else 0
        )

        blank_charges = int(
            customer_data["TotalCharges_numeric"].isna().sum()
        )

        k1, k2, k3, k4 = st.columns(4)

        k1.metric(
            "Total customers",
            f"{total_customers:,}",
        )

        k2.metric(
            "Churned customers",
            f"{churned_count:,}",
            f"{churn_rate:.1f}%",
        )

        k3.metric(
            "Retained customers",
            f"{retained_count:,}",
            f"{retained_rate:.1f}%",
        )

        k4.metric(
            "Missing total charges",
            f"{blank_charges:,}",
        )

        st.divider()

        left, right = st.columns(2, gap="large")

        with left:
            st.markdown("#### Customer outcomes")

            outcome = pd.Series(
                {
                    "Retained": retained_count,
                    "Churned": churned_count,
                }
            )

            st.bar_chart(
                outcome,
                horizontal=True,
            )

        with right:
            st.markdown("#### Churn by contract")

            contract_rates = (
                customer_data.assign(
                    ChurnFlag=churn_flag.astype(int)
                )
                .groupby("Contract")["ChurnFlag"]
                .mean()
                .mul(100)
                .sort_values(ascending=False)
                .rename("Churn rate (%)")
            )

            st.bar_chart(
                contract_rates,
                horizontal=True,
            )

        left, right = st.columns(2, gap="large")

        with left:
            st.markdown("#### Churn by internet service")

            internet_rates = (
                customer_data.assign(
                    ChurnFlag=churn_flag.astype(int)
                )
                .groupby("InternetService")["ChurnFlag"]
                .mean()
                .mul(100)
                .sort_values(ascending=False)
                .rename("Churn rate (%)")
            )

            st.bar_chart(
                internet_rates,
                horizontal=True,
            )

        with right:
            st.markdown("#### Churn by payment method")

            payment_rates = (
                customer_data.assign(
                    ChurnFlag=churn_flag.astype(int)
                )
                .groupby("PaymentMethod")["ChurnFlag"]
                .mean()
                .mul(100)
                .sort_values(ascending=False)
                .rename("Churn rate (%)")
            )

            st.bar_chart(
                payment_rates,
                horizontal=True,
            )

        st.divider()

        st.markdown("#### Customer behaviour")

        avg_tenure_churn = pd.to_numeric(
            customer_data.loc[churn_flag, "tenure"],
            errors="coerce",
        ).mean()

        avg_tenure_stay = pd.to_numeric(
            customer_data.loc[stay_flag, "tenure"],
            errors="coerce",
        ).mean()

        avg_monthly_churn = pd.to_numeric(
            customer_data.loc[churn_flag, "MonthlyCharges"],
            errors="coerce",
        ).mean()

        avg_monthly_stay = pd.to_numeric(
            customer_data.loc[stay_flag, "MonthlyCharges"],
            errors="coerce",
        ).mean()

        a, b, c = st.columns(3)

        a.metric(
            "Avg. tenure · churned",
            f"{avg_tenure_churn:.1f} months",
        )

        b.metric(
            "Avg. tenure · retained",
            f"{avg_tenure_stay:.1f} months",
        )

        c.metric(
            "Avg. monthly charges · churned",
            f"${avg_monthly_churn:.2f}",
        )

        st.caption(
            f"Retained customers average "
            f"${avg_monthly_stay:.2f} in monthly charges. "
            "These are descriptive associations, not proof of causation."
        )

        with st.expander("View customer records"):
            st.dataframe(
                customer_data.drop(
                    columns=["TotalCharges_numeric"]
                ),
                use_container_width=True,
                hide_index=True,
            )

            st.caption(
                f"Dataset file: {dataset_path}"
            )


# ============================================================
# PAGE 3: ABOUT
# ============================================================

elif page == "About":

    st.markdown(
        '<div class="page-title">About this project</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="page-description">
            A machine learning application designed to estimate
            telecom customer churn and help explore the patterns
            associated with customer retention.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("### Project overview")

    st.write(
        "Customer churn prediction is a binary classification task. "
        "The application accepts customer demographics, account "
        "tenure, subscribed services, contract information and "
        "billing details, then uses a trained model to estimate "
        "the probability of churn."
    )

    st.divider()

    st.markdown("### Technology stack")

    st.markdown(
        """
        - **Python** — application logic
        - **Streamlit** — web interface
        - **Pandas** — data processing
        - **Scikit-learn** — preprocessing and prediction
        - **Joblib** — loading saved model artifacts
        """
    )

    st.divider()

    st.markdown("### Dataset")

    st.write(
        "IBM Telco Customer Churn dataset, containing information "
        "about customer accounts, services, contracts, payments "
        "and recorded churn outcomes."
    )

    st.divider()

    st.markdown("### Model evaluation")

    metric1, metric2 = st.columns(2)

    metric1.metric("Reported recall", "0.80")
    metric2.metric("Reported ROC-AUC", "0.84")

    st.caption(
        "These are project-reported benchmark figures. "
        "They are not recalculated or independently verified by this app."
    )

    st.divider()

    st.markdown("### Important note")

    st.write(
        "Predictions are estimates based on patterns learned "
        "from training data. They should support further analysis "
        "and human decision-making rather than be treated as "
        "certain outcomes."
    )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">
        Customer Insights · Customer Churn Prediction<br>
        Built with Python, Streamlit, Pandas and Scikit-learn<br>
        Academic portfolio project
    </div>
    """,
    unsafe_allow_html=True,
)
