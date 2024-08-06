import streamlit as st

def summary2():
    st.title("Summary by AI")
    
    st.markdown("<h2 style='color: green;'>ผลกระทบหลังจากผ่านร่างกฎหมายแรงงานใหม่</h2>", unsafe_allow_html=True)
    
    st.markdown("<h3 style='color: blue;'>ผลดี</h3>", unsafe_allow_html=True)
    st.markdown("""
    <ul>
        <li><strong>การคุ้มครองสิทธิแรงงาน:</strong> ร่างกฎหมายใหม่จะให้ความคุ้มครองสิทธิพื้นฐานของแรงงานทุกคน รวมถึงสิทธิในการรวมตัวและเจรจาต่อรองร่วม ซึ่งจะช่วยลดการเอารัดเอาเปรียบและเพิ่มความเป็นธรรมในที่ทำงาน</li>
        <li><strong>การลดข้อขัดแย้งแรงงาน:</strong> ด้วยการส่งเสริมระบบแรงงานสัมพันธ์ที่ดี ร่างกฎหมายนี้จะช่วยลดข้อพิพาทและความขัดแย้งระหว่างคนทำงานและผู้จ้างงาน ซึ่งจะส่งผลดีต่อการทำงานร่วมกันอย่างสันติและมีประสิทธิภาพ</li>
        <li><strong>การยกระดับมาตรฐานแรงงาน:</strong> การปรับปรุงกฎหมายให้สอดคล้องกับมาตรฐานแรงงานสากลจะช่วยให้ประเทศไทยได้รับการยอมรับจากนานาชาติ ซึ่งสามารถส่งผลดีต่อการค้าและการลงทุน</li>
        <li><strong>การส่งเสริมเศรษฐกิจที่ยั่งยืน:</strong> การสร้างระบบแรงงานที่ยุติธรรมจะช่วยส่งเสริมการพัฒนาเศรษฐกิจที่ยั่งยืน โดยคนทำงานและผู้จ้างงานสามารถทำงานร่วมกันอย่างมีความสุขและมีประสิทธิภาพ</li>
    </ul>
    """, unsafe_allow_html=True)
    
    st.markdown("<h3 style='color: red;'>ผลเสีย</h3>", unsafe_allow_html=True)
    st.markdown("""
    <ul>
        <li><strong>ความท้าทายในการปรับตัว:</strong> ผู้จ้างงานอาจต้องใช้เวลาและทรัพยากรในการปรับตัวให้สอดคล้องกับกฎหมายใหม่ ซึ่งอาจสร้างความยุ่งยากในระยะแรก</li>
        <li><strong>การบริหารจัดการที่ซับซ้อน:</strong> การบังคับใช้กฎหมายใหม่อาจต้องมีการบริหารจัดการที่ซับซ้อนกว่าเดิม โดยเฉพาะการกำกับดูแลและตรวจสอบให้เป็นไปตามกฎหมาย</li>
        <li><strong>ต้นทุนทางธุรกิจ:</strong> ผู้ประกอบการอาจต้องเผชิญกับต้นทุนที่เพิ่มขึ้นจากการปฏิบัติตามกฎหมายใหม่ เช่น การปรับปรุงสวัสดิการและค่าจ้างให้เป็นไปตามมาตรฐานใหม่</li>
        <li><strong>ความเสี่ยงต่อการฟ้องร้อง:</strong> หากมีการตีความกฎหมายที่ไม่ชัดเจนหรือการบังคับใช้ที่ไม่เท่าเทียม อาจนำไปสู่การฟ้องร้องและข้อพิพาททางกฎหมายมากขึ้น</li>
    </ul>
    """, unsafe_allow_html=True)
    
    st.markdown("<h3 style='color: purple;'>สรุป</h3>", unsafe_allow_html=True)
    st.markdown("""
    การผ่านร่างกฎหมายแรงงานใหม่จะช่วยเพิ่มความเป็นธรรมและคุ้มครองสิทธิของคนทำงาน ส่งเสริมการพัฒนาเศรษฐกิจและสังคมที่ยั่งยืน แต่ในขณะเดียวกัน ก็อาจสร้างความท้าทายและภาระใหม่ในการปรับตัวและการบริหารจัดการที่มีประสิทธิภาพสำหรับผู้จ้างงานและภาครัฐ.
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    summary2()