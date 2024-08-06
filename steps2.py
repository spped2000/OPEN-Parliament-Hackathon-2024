import streamlit as st
import streamlit_antd_components as sac
import random
from streamlit_feedback import streamlit_feedback

def run():
    st.title("ร่างพระราชบัญญัติสหภาพแรงงาน")
    st.write("เนื่องจากพระราชบัญญัติแรงงานสัมพันธ์ พ.ศ. 2518 ได้ใช้บังคับมาเป็นเวลานาน บทบัญญัติหลายประการไม่เหมาะสมกับสภาพการในปัจจุบันและไม่สอดคล้องกับหลักการที่เป็นมาตรฐานแรงงานสากล โดยเฉพาะอย่างยิ่ง หลายมาตรายังขัดกับหลักการในอนุสัญญาองค์การแรงงานระหว่างประเทศ ฉบับที่ 87 และ 89 ที่ว่าด้วยเสรีภาพในการรวมตัวและการเจรจาต่อรองและถูกกำหนดให้เป็นอนุสัญญาหลัก เป็นสิทธิแรงงานขั้นพื้นฐานที่ต้องได้รับการปกป้องคุ้มครองและส่งเสริมอย่างจริงจัง จึงเป็นเหตุให้คนทำงานและผู้จ้างงานส่วนใหญ่ไม่สามารถเข้าถึงสิทธิดังกล่าวได้จริง ภายใต้พระราชบัญญัติแรงงานสัมพันธ์ พ.ศ. 2518 ยังมีข้อจำกัดที่จะทำให้เกิดระบบแรงงานสัมพันธ์ที่ดีระหว่างคนทำงานและผู้จ้างงานได้ ดังจะเห็นว่ามีปัญหาข้อขัดแย้งและข้อพิพาทด้านแรงงานจำนวนมาก และหลายครั้งที่ความขัดแย้งและข้อพิพาทได้นำสู่ การต่อสู้เผชิญหน้ากันอย่างรุนแรง สร้างความเสียหายให้กับทั้งคนทำงาน ผู้จ้างงาน และประเทศชาติโดยรวมสิทธิในการรวมตัว เจรจาต่อรองร่วมถือเป็นสิทธิขั้นพื้นฐานที่สำคัญของพลเมืองในระบอบประชาธิปไตย สิทธิดังกล่าวมีการรับรองไว้ในอนุสัญญาและกติการะหว่างประเทศว่าด้วยสิทธิมนุษยชนหลายฉบับ ที่สำคัญคืออนุสัญญาขององค์การแรงงานระหว่างประเทศ ฉบับที่ 87 ว่าด้วยเสรีภาพในการสมาคม และฉบับที่ 98 ว่าด้วยสิทธิในการรวมตัวและเจรจาต่อรองร่วม ประเทศไทยแม้รัฐธรรมนูญจะมีบทบาท ที่รับรองสิทธิในการรวมตัวกันของประชาชน แต่กฎหมายลำดับรอง ที่มีอยู่ไม่ว่าจะเป็นพระราชบัญญัติแรงงานสัมพันธ์ พ.ศ. 2518 และพระราชบัญญัติแรงงานรัฐวิสาหกิจสัมพันธ์ พ.ศ. 2543 ล้วนยังมีสาระสำคัญ ที่ไม่สอดคล้องกับหลักการของอนุสัญญาดังกล่าว กฎหมายครอบคลุมเฉพาะแรงงานในระบบกับพนักงานรัฐวิสาหกิจเท่านั้น ยังมีคนทำงานอีกมากมายทั้งที่ถูกเรียกว่า แรงงานนอกระบบ ข้าราชการ ลูกจ้างรัฐที่ไม่ได้รับการคุ้มครองโดยกฎหมายดังกล่าว เป็นเหตุให้คนทำงานในประเทศไทยส่วนใหญ่ไม่สามารถเข้าถึงสิทธิ ในการรวมตัวและเจรจาต่อรองร่วมได้อย่างแท้จริง ทำให้ประเทศกลายเป็นประเทศที่คนทำงานเป็นสมาชิกสหภาพแรงงานในอัตราที่ต่ำที่สุดของโลกหรือราวร้อยละ 1.5 เท่านั้น และการที่คนงานส่วนใหญ่ไม่สามารถรวมตัวและทำการเจรจาต่อรองร่วมได้ ทำให้คนทำงานต้องถูกเอารัดเอาเปรียบ ไม่ได้รับความเป็นธรรม มีค่าจ้างต่ำ สวัสดิการที่เลวร้าย ต้องทำงานหนักและยาวนานในแต่ละวัน และเป็นสาเหตุสำคัญที่ทำให้ ประเทศไทยเป็นประเทศที่มีความเหลื่อมล้ำเป็นอันดับต้น ๆ ของโลกด้วยเพื่อให้กฎหมายมีหลักการและสาระที่สอดรับกับสภาพแวดล้อมทั้งทางการเมือง เศรษฐกิจ และสังคมที่เปลี่ยนไปอย่างมาก เพื่อให้สอดคล้องกับมาตรฐานและหลักการอันเป็นสากลที่มีความสำคัญ อย่างยิ่งต่อการยอมรับของนานาอารยะประเทศ และเพื่อส่งเสริมให้เกิดระบบแรงงานสัมพันธ์ที่คนทำงาน และผู้จ้างงานสามารถทำงานร่วมกันด้วยความพอใจอย่างสันติสุข และต่างได้รับความเป็นธรรม และที่สำคัญ คือสามารถนำสู่การพัฒนาเศรษฐกิจที่ยั่งยืน และสร้างสังคมที่เป็นธรรม เสมอภาค จึงเห็นสมควร ให้มีการยกร่างพระราชบัญญัติสหภาพแรงงาน พ.ศ. .... ฉบับนี้ขึ้น")

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
            st.experimental_set_query_params(page="summary2")
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
            # st.write(f"Feedback: {feedback}")

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
