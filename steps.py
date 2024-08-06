import streamlit as st
import streamlit_antd_components as sac
import random
from streamlit_feedback import streamlit_feedback

def run():
    st.title("ร่างพระราชบัญญัติป่าสงวนแห่งชาติ")
    st.write("พระราชบัญญัติป่าสงวนแห่งชาติ พ.ศ. 2507 มีบทบัญญัติที่ขัดกับรัฐธรรมนูญไทยในเรื่องสิทธิชุมชน ทำให้เกิดข้อพิพาทระหว่างประชาชนและรัฐ รัฐควรช่วยประชาชนที่ครอบครองที่ดินมาก่อนประกาศเป็นเขตป่าสงวน สามารถทำกินและอยู่อาศัยได้โดยไม่ถือว่าผิดกฎหมาย และให้องค์กรปกครองท้องถิ่นมีอำนาจพิจารณาความเหมาะสมในการออกหนังสือรับรองการครอบครอง เพื่อสอดคล้องกับรัฐธรรมนูญและสภาพพื้นที่จริง จำเป็นต้องแก้ไขพระราชบัญญัตินี้")

    sac.steps(
        items=[
            sac.StepsItem(title='เสนอร่างแก้ไข', description='โดย สส.', disabled=True),
            sac.StepsItem(title='ธุรการ', disabled=True),
            sac.StepsItem(title='บรรจุเข้าสภา', disabled=True),
        ], index=3, color='green'
    )
    sac.steps(
        items=[
            sac.StepsItem(title='สส. วาระ 1', description='รับหลักการ', disabled=True),
            sac.StepsItem(title='สส. วาระ 2', description='พิจารณารายมาตรา', disabled=True),
            sac.StepsItem(title='สส. วาระ 3', description='ลงมติทั้งฉบับ', disabled=True),
        ], index=3, color='green'
    )
    sac.steps(
        items=[
            sac.StepsItem(title='สว. วาระ 1', description='รับหลักการ', disabled=True),
            sac.StepsItem(title='สว. วาระ 2', description='พิจารณารายมาตรา', disabled=True),
            sac.StepsItem(title='สว. วาระ 3', description='ลงมติทั้งฉบับ', disabled=True),
        ], index=3, color='green'
    )

    # Add buttons in the same line
    col1, col2 = st.columns([1, 1])
    with col1:
        st.link_button("Open Link to Read More", "https://www.parliament.go.th/section77/survey_detail.php?id=396")
    with col2:
        if st.button("Summary by AI"):
            st.experimental_set_query_params(page="summary")
            st.experimental_rerun()

    # List of random Thai names and comments about กฎหมายสมรสเท่าเทียม
    thai_names = ["สมชาย", "สมหญิง", "นพพร", "จิราภรณ์", "กิตติ", "จารุวรรณ"]
    thai_comments = [
        "ผมสนับสนุนกฎหมายสัตว์ป่าเพราะเป็นการคุ้มครองสัตว์ที่สำคัญและจำเป็น",
        "การมีกฎหมายสัตว์ป่าจะทำให้เราสามารถอนุรักษ์สัตว์และสิ่งแวดล้อมได้ดียิ่งขึ้น",
        "กฎหมายสัตว์ป่าเป็นสิ่งที่ควรมีมานานแล้วเพื่อปกป้องสัตว์ที่ใกล้สูญพันธุ์",
        "เราควรให้ความสำคัญในการปกป้องสัตว์ป่าเพื่อรักษาความหลากหลายทางชีวภาพ",
        "การมีกฎหมายสัตว์ป่าเป็นก้าวสำคัญในการอนุรักษ์ธรรมชาติและสร้างความยั่งยืนในระบบนิเวศ",
        "กฎหมายสัตว์ป่าจะช่วยให้สัตว์ทุกชนิดมีโอกาสในการมีชีวิตที่ปลอดภัยและสุขภาพดี"
    ]

    # Generate a list of 5 initial comments
    if 'comments' not in st.session_state:
        st.session_state.comments = [
            {"name": random.choice(thai_names), "text": random.choice(thai_comments), "thumbs_up": random.randint(1, 100), "thumbs_down": random.randint(1, 100)}
            for _ in range(5)
        ]

    # Function to display comments
    def display_comments():
        for i, comment in enumerate(st.session_state.comments):
            st.markdown(f"""
            <div style="border: 1px solid #e1e1e1; padding: 10px; border-radius: 5px; margin-bottom: 10px;">
                <strong>{comment['name']}</strong>: {comment['text']}
                <div style="display: flex; align-items: center; gap: 10px;">
                    <span>👍 {comment['thumbs_up']}</span>
                    <span>👎 {comment['thumbs_down']}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
            feedback = streamlit_feedback(feedback_type="thumbs", align="flex-start", key=f"feedback_{i}")
            if feedback:
                if feedback == "👍":
                    st.session_state.comments[i]["thumbs_up"] += 1
                elif feedback == "👎":
                    st.session_state.comments[i]["thumbs_down"] += 1
                st.experimental_rerun()

    # Display existing comments
    st.subheader("Comments")
    display_comments()

    # Comment input section
    st.subheader("Add a Comment")
    name = "นาย รัฐสภา โปร่งใส"
    st.markdown(f"**Commenting as:** {name}")
    comment_text = st.text_area("Comment")

    # Button to submit the comment
    if st.button("Submit Comment"):
        if comment_text:
            new_comment = {"name": name, "text": comment_text, "thumbs_up": 0, "thumbs_down": 0}
            st.session_state.comments.append(new_comment)
            # Clear input fields after submission
            st.experimental_rerun()
        else:
            st.warning("Please enter a comment before submitting.")

    if st.button("กลับไปหน้าหลัก"):
        st.experimental_set_query_params(page="home")
        st.experimental_rerun()

if __name__ == "__main__":
    run()
