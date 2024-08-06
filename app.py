import streamlit as st

def main():
    # List of laws to track
    laws = [
        "ร่างพระราชบัญญัติป่าสงวนแห่งชาติ",
        "ร่างพระราชบัญญัติสหภาพแรงงาน",
        "ร่างพระราชบัญญัติกัญชา กัญชง"
    ]

    # Descriptions for each law
    law_descriptions = {
        "ร่างพระราชบัญญัติป่าสงวนแห่งชาติ": "พระราชบัญญัติป่าสงวนแห่งชาติ พ.ศ. 2507 มีบทบัญญัติที่ขัดกับรัฐธรรมนูญไทยในเรื่องสิทธิชุมชน ทำให้เกิดข้อพิพาทระหว่างประชาชนและรัฐ รัฐควรช่วยประชาชนที่ครอบครองที่ดินมาก่อนประกาศเป็นเขตป่าสงวน สามารถทำกินและอยู่อาศัยได้โดยไม่ถือว่าผิดกฎหมาย และให้องค์กรปกครองท้องถิ่นมีอำนาจพิจารณาความเหมาะสมในการออกหนังสือรับรองการครอบครอง เพื่อสอดคล้องกับรัฐธรรมนูญและสภาพพื้นที่จริง จำเป็นต้องแก้ไขพระราชบัญญัตินี้",
        "ร่างพระราชบัญญัติสหภาพแรงงาน": "",
        "ร่างพระราชบัญญัติกัญชา กัญชง": ""
    }

    # Mapping of laws to steps pages
    steps_mapping = {
        "ร่างพระราชบัญญัติป่าสงวนแห่งชาติ": "steps",
        "ร่างพระราชบัญญัติสหภาพแรงงาน": "steps2",
        "ร่างพระราชบัญญัติกัญชา กัญชง": "steps3"
    }

    # Set up the Streamlit web app
    st.title("ติดตามร่างกฎหมาย")
    st.write("เลือกกฎหมายที่คุณต้องการติดตามและใช้ช่องค้นหาเพื่อค้นหากฎหมายเฉพาะ")

    # Dropdown to select laws
    selected_laws = st.selectbox("เลือกกฎหมายที่ต้องการติดตาม:", laws)

    # Display the description of the selected law
    st.write("คำอธิบายของกฎหมายที่เลือก:")
    st.write(law_descriptions[selected_laws])

    # Button to move to the corresponding steps page
    if st.button("ไปยังขั้นตอน"):
        st.experimental_set_query_params(page=steps_mapping[selected_laws])
        st.experimental_rerun()

def steps():
    import steps
    steps.run()

def steps2():
    import steps2
    steps2.run()

def steps3():
    import steps3
    steps3.run()

def summary():
    import summary
    summary.summary()

def summary2():
    import summary2
    summary2.summary2()

def summary3():
    import summary3
    summary3.summary3()

pages = {
    "home": main,
    "steps": steps,
    "steps2": steps2,
    "steps3": steps3,
    "summary": summary,
    "summary2": summary2,
    "summary3": summary3
}

def add_logo():
    st.markdown(
        """
        <style>
        [data-testid="stSidebar"] {
            display: none;
        }
        .logo {
            position: fixed;
            top: 10px;
            right: 10px;
            width: 100px;
            height: auto;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    # Temporary display for verification
    st.image("Logo_White.png", width=100)
    st.markdown(
        """
        <img src="Logo_White.png" class="logo">
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    add_logo()
    query_params = st.experimental_get_query_params()
    page = query_params.get("page", ["home"])[0]
    if page in pages:
        pages[page]()
    else:
        main()
