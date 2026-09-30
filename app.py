import streamlit as st
import pandas as pd
import plotly.express as px
from io import BytesIO

# 和GitHub仓库文件名严格一致，全部jpg
banner_path = "banner_rootbloom_grass.jpg"
perma_path = "perma_model.jpg"

st.set_page_config(
    page_title="从文化符号到品质行为",
    page_icon="🌱",
    layout="wide"
)

page_style = """
<style>
[data-testid="stAppViewContainer"] {
    background-color: #f7f1e3;
}
.banner-fallback{
    width:100%;
    padding:40px 20px;
    text-align:center;
}
.banner-fallback-title{
    font-size:34px;
    font-weight:bold;
    color:#2c4227;
}
[data-testid="stHeader"] {
    background-color: rgba(0,0,0,0) !important;
}
.nav-container {
    background-color: rgba(255,255,255,0.85);
    padding:14px 18px;
    border-radius:14px;
    margin-bottom:18px;
    box-shadow:0 2px 8px rgba(0,0,0,0.07);
}
.content-card {
    background-color:#e8f1e4;
    padding:26px;
    border-radius:14px;
    margin-bottom:20px;
    box-shadow:0 3px 10px rgba(0,0,0,0.06);
}
</style>
"""
st.markdown(page_style, unsafe_allow_html=True)

# Banner，读取失败自动显示文字标题
try:
    st.image(banner_path, use_container_width=True)
except Exception:
    st.markdown("""
    <div class="banner-fallback">
        <div class="banner-fallback-title">从文化符号到品质行为｜RootBloom乡土育人项目</div>
    </div>
    """, unsafe_allow_html=True)

# 顶部横向导航栏
st.markdown("<div class='nav-container'>", unsafe_allow_html=True)
page = st.radio(
    "",
    ["首页", "PERMA框架｜品质行为观测体系", "AI校本课程开发（自定义乡土载体）", "乡土校本课程案例库", "品质行为前后对比评估", "学生品质行为成长档案"],
    horizontal=True
)
st.markdown("</div>", unsafe_allow_html=True)
st.markdown("<hr style='border:1px solid #b8c9b3;'>", unsafe_allow_html=True)

# ====================== 首页 ======================
if page == "首页":
    st.markdown("<div class='content-card'>", unsafe_allow_html=True)
    st.subheader("从文化符号到品质行为 — RootBloom乡土育人项目")
    st.write("本项目核心逻辑：**乡土文化符号是育人载体，学生品质行为变化是评价核心**。不同本土文化符号素材，承载的育人方向各不相同，不会用同一套目标套用全部校本资源。")
    st.write("依托PERMA积极心理学框架，把抽象德育目标转化为课堂上可观察、可记录的学生品质行为。教师可以根据学校本土特色文化符号（竹子、木棉花、簕杜鹃、红色乡土故事等），定制对应的校本课程，追踪课程实施前后学生品质行为的真实改变。")

    st.subheader("项目背景")
    st.write("乡村小学德育普遍存在痛点：德育课程容易同质化，不管什么乡土文化符号，育人目标全部一刀切；德育评价偏向主观评语，缺少对学生真实行为的过程追踪；校本课程开发工作量大，一线教师很难独立完成完整设计。")
    st.write("本工具解决该问题：**文化载体自定义，品质行为目标随载体调整**。以可观测的课堂行为作为评价依据，记录、可视化学生在乡土实践中的成长变化，证明文化符号浸润带来的行为改变。")

    st.subheader("项目核心目标")
    st.write("1. 理论目标：建立适配乡土课堂的PERMA品质行为观测体系，实现德育评价从主观感受，转向可观测的学生行为记录。")
    st.write("2. 课程开发目标：支持教师自选本土文化符号载体，生成差异化校本课程，每一类乡土素材匹配专属的品质培育方向。")
    st.write("3. 工具目标：搭建网页辅助平台，辅助教师备课、记录课堂行为、可视化对比成长、导出学生品质成长档案。")
    st.write("4. 育人目标：依托在地乡土文化体验，引导学生建立乡土认同，在实践中养成友善、专注、合作、自信的稳定品质行为。")
    st.markdown("</div>", unsafe_allow_html=True)

# ====================== PERMA框架｜品质行为观测体系 ======================
elif page == "PERMA框架｜品质行为观测体系":
    st.markdown("<div class='content-card'>", unsafe_allow_html=True)
    try:
        st.image(perma_path, use_container_width=True)
    except Exception:
        st.info("📌 PERMA品质行为观测框架示意图")

    st.subheader("PERMA框架：五大可观测品质行为维度")
    st.write("本框架不做固定课程内容，**不同乡土文化符号载体，侧重激活不同的品质行为**：")
    st.write("🌞 P 积极情绪｜共情感恩、友善待人：体会自然与人文之美，共情他人，懂得感恩。")
    st.write("🎯 E 投入专注｜坚持不懈、踏实坚韧：面对探究任务愿意持续投入，遇到困难不轻易放弃。")
    st.write("🤝 R 人际关系｜尊重倾听、协作互助：小组活动倾听伙伴，分工合作，包容不同想法。")
    st.write("🧭 M 意义认同｜乡土归属感、文化自信：理解家乡本土文化符号，建立对本土资源的认同与珍视。")
    st.write("🏅 A 成就自信｜勇于表达、敢于挑战：愿意展示成果，主动分享，在实践中收获成就感。")

    st.subheader("不同乡土文化符号，差异化育人侧重点（不再一刀切）")
    st.write("🎋 **竹子（文化符号）**：重点侧重【E专注坚持 + M乡土认同】。竹子坚韧不拔、四季常青，引导学生理解坚韧品格，感受本土植物生命力量，磨炼持之以恒的品质。")
    st.write("🌺 **木棉花（文化符号）**：重点侧重【P共情感恩 + A自信表达】。英雄花木棉，扎根故土、向阳绽放，引导学生感悟奉献精神，敢于表达对家乡的热爱。")
    st.write("🌿 **簕杜鹃（文化符号）**：重点侧重【R协作互助 + M乡土认同】。簕杜鹃丛生盛放，抱团生长，引导学生理解团结协作，感受乡土生命力。")
    st.write("📜 **东江红色乡土故事（文化符号）**：重点侧重【M乡土认同 + E坚韧坚持】，感悟先辈坚守，厚植家国情怀，培育不怕困难的意志品质。")

    st.write("教师在设计课程时，根据选用的乡土文化符号素材，选择对应的重点培育维度，在课堂中针对性观察、记录学生的对应品质行为。")
    st.markdown("</div>", unsafe_allow_html=True)

# ====================== AI校本课程开发（自定义乡土载体） ======================
elif page == "AI校本课程开发（自定义乡土载体）":
    st.markdown("<div class='content-card'>", unsafe_allow_html=True)
    st.subheader("🤖 AI校本课程提示词生成器｜自定义乡土文化符号载体")
    st.write("选择你的学校本土文化符号素材，系统自动匹配对应的核心品质行为方向，生成专属校本课程，附带配套课堂品质行为观察量表。")

    col1, col2 = st.columns(2)
    with col1:
        grade_sel = st.selectbox("授课年级", ["三年级","四年级","五年级","六年级"])
        local_culture = st.selectbox("本土乡土文化符号载体", ["竹子文化","木棉花文化","簕杜鹃文化","东江红色乡土故事","其他（自定义输入）"])
        if local_culture == "其他（自定义输入）":
            local_culture = st.text_input("输入你的校本文化主题", value="")
    with col2:
        lesson_num = st.number_input("总课时数量", min_value=1,max_value=10,value=2)

    if "竹子" in local_culture:
        default_dim = ["E专注坚持","M乡土认同"]
    elif "木棉花" in local_culture:
        default_dim = ["P共情感恩","A自信表达"]
    elif "簕杜鹃" in local_culture:
        default_dim = ["R协作互助","M乡土认同"]
    elif "红色" in local_culture:
        default_dim = ["E专注坚持","M乡土认同"]
    else:
        default_dim = ["P共情感恩","M乡土认同"]

    perma_dim = st.multiselect("重点培育品质行为维度（可自行修改）",
        ["P共情感恩","E专注坚持","R协作互助","M乡土认同","A自信表达"],
        default=default_dim)

    dim_text = ', '.join(perma_dim)
    prompt = f"""
请为小学{grade_sel}设计{lesson_num}课时的乡土校本德育课程，校本文化符号载体：{local_culture}。
课程依托本地乡土资源，以PERMA框架为基础，重点培育学生品质行为：{dim_text}。
课程设计核心：乡土文化符号为载体，目标聚焦学生课堂可观测品质行为，拒绝一刀切德育模板。

要求输出完整课程方案：
1.课程设计理念：结合{local_culture}本身的文化内涵，挖掘独有的育人价值，把文化符号认知转化为学生可观测的品质行为。
2.核心素养目标：重点写**可观察的学生行为目标**，不写空泛文字。
3.教学重难点，贴合该乡土素材的特点。
4.分课时教学设计：教学环节、时长、学生实践活动、教师引导话术。
5.配套课堂品质行为观察量表：只记录课堂上可以亲眼观察到的学生行为，对应PERMA维度，用于课后评估学生品质行为变化。
6.课堂实施注意事项、本土化素材采集建议。

面向乡村小学，体验式实践课程，拒绝纯说教，适合校本课程申报。
"""
    st.subheader("✅ 生成的AI提示词（全选复制发给豆包）")
    st.code(prompt, language="text")
    st.info("💡 使用方法：复制全部文本，发给豆包，直接生成贴合你所选乡土文化符号的定制教案+行为观察量表。")

    st.subheader("🎨 AI辅助素材制作")
    st.write("- AI绘制对应乡土文化符号插画（竹子/木棉花等），用于课件、课堂任务单。")
    st.write("- 生成课堂情景对话脚本，用于德育角色扮演活动。")

    st.subheader("💬 AI课堂互动引导")
    st.write("- 课堂作为辅助角色，引导学生探究本土文化符号，启发学生思考对应的品质。")
    st.write("- 教师全程主导课堂，AI仅作为备课与课堂辅助工具。")
    st.markdown("</div>", unsafe_allow_html=True)

# ====================== 乡土校本课程案例库 ======================
elif page == "乡土校本课程案例库":
    st.markdown("<div class='content-card'>", unsafe_allow_html=True)
    st.subheader("📚 差异化乡土校本课程案例库")
    st.write("每一套案例，都基于乡土文化符号本身内涵，匹配专属的品质行为培育重点，不套用同一套育人目标。")

    st.subheader("🎋 案例1：竹子乡土文化课程｜重点：E专注坚持 + M乡土认同")
    st.write("文化符号内涵：竹子宁折不弯、节节向上，扎根山野。课程以观察本地竹林、竹艺手作为实践活动。")
    st.write("品质观测重点：观察学生面对手工困难时是否坚持不懈；体会竹子品格，建立对家乡植物资源的认同。")
    st.write("课堂活动：竹林实地观察、竹艺手工、竹子故事分享。")

    st.subheader("🌺 案例2：木棉花乡土文化课程｜重点：P共情感恩 + A自信表达")
    st.write("文化符号内涵：木棉花被誉为英雄花，向阳盛放，落地依然保持风骨。")
    st.write("品质观测重点：引导学生感悟奉献精神；鼓励学生主动上台分享感悟，锻炼自信表达、共情感恩。")
    st.write("课堂活动：木棉花标本采集、诗歌品读、成果主题分享会。")

    st.subheader("🌿 案例3：簕杜鹃乡土文化课程｜重点：R协作互助 + M乡土认同")
    st.write("文化符号内涵：簕杜鹃成片丛生，抱团绽放，生命力顽强。")
    st.write("品质观测重点：小组合作探究，观察学生倾听、分工、互助的协作行为；感受本土植物蓬勃生命力，建立乡土归属感。")
    st.write("课堂活动：小组研学、集体创作乡土海报。")

    st.subheader("📜 案例4：东江红色乡土故事课程｜重点：E坚韧坚持 + M乡土认同")
    st.write("文化符号内涵：东江纵队先辈在家乡坚守抗争，不畏艰难。")
    st.write("品质观测重点：体会先辈坚韧不屈的品质；建立家乡历史认同感，培养责任意识。")
    st.write("课堂活动：红色故事研读、情景研学、感悟分享。")

    st.write("教师可以直接选用案例，或者使用上一页AI生成器，创建属于本校独有的乡土课程方案。课程结束后，录入课堂观察分数，评估学生品质行为成长。")
    st.markdown("</div>", unsafe_allow_html=True)

# ====================== 品质行为前后对比评估 ======================
elif page == "品质行为前后对比评估":
    st.markdown("<div class='content-card'>", unsafe_allow_html=True)
    st.subheader("📊 学生品质行为｜课程实施前后对比")
    st.write("填入课程开展前、课程结束后的课堂观察打分（满分10分）。**根据你这门课的乡土文化符号载体，重点关注对应维度的分数变化**，直观看到学生品质行为的成长。")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("课程前：行为表现得分（满分10）")
        pre_P = st.number_input("P 共情感恩", min_value=0.0, max_value=10.0, value=4.2, step=0.1)
        pre_E = st.number_input("E 专注坚持", min_value=0.0, max_value=10.0, value=3.8, step=0.1)
        pre_R = st.number_input("R 协作互助", min_value=0.0, max_value=10.0, value=4.0, step=0.1)
        pre_M = st.number_input("M 乡土认同", min_value=0.0, max_value=10.0, value=3.5, step=0.1)
        pre_A = st.number_input("A 自信表达", min_value=0.0, max_value=10.0, value=3.6, step=0.1)

    with col2:
        st.subheader("课程后：行为表现得分（满分10）")
        post_P = st.number_input("P 共情感恩", min_value=0.0, max_value=10.0, value=7.1, step=0.1)
        post_E = st.number_input("E 专注坚持", min_value=0.0, max_value=10.0, value=6.8, step=0.1)
        post_R = st.number_input("R 协作互助", min_value=0.0, max_value=10.0, value=7.3, step=0.1)
        post_M = st.number_input("M 乡土认同", min_value=0.0, max_value=10.0, value=7.5, step=0.1)
        post_A = st.number_input("A 自信表达", min_value=0.0, max_value=10.0, value=6.9, step=0.1)

    data = pd.DataFrame({
        "品质行为维度": ["共情感恩P", "专注坚持E", "协作互助R", "乡土认同M", "自信表达A"] * 2,
        "行为得分": [pre_P, pre_E, pre_R, pre_M, pre_A, post_P, post_E, post_R, post_M, post_A],
        "阶段": ["课程前","课程前","课程前","课程前","课程前","课程后","课程后","课程后","课程后","课程后"]
    })
    fig = px.bar(data, x="品质行为维度", y="行为得分", color="阶段", barmode="group",
                 range_y=[0,10], title="乡土校本课程实施｜学生品质行为前后对比")
    st.plotly_chart(fig, use_container_width=True)
    st.write("💡分析提示：重点观察这门乡土课程**选定的核心维度**的分数涨幅，以此证明本次文化符号浸润对学生品质行为带来的改变。")
    st.markdown("</div>", unsafe_allow_html=True)

# ====================== 学生品质行为成长档案 ======================
elif page == "学生品质行为成长档案":
    st.markdown("<div class='content-card'>", unsafe_allow_html=True)
    st.subheader("📒 学生品质行为成长档案记录系统")
    st.write("教师基于乡土课堂现场观察，记录学生品质行为表现。支持单学生录入、全班表格批量上传，自动生成**贴合本次乡土文化符号课程的个性化行为评语**，一键导出全班Excel档案。")

    def generate_comment(p,e,r,m,a):
        score_list = [("共情感恩",p),("专注坚持",e),("协作互助",r),("乡土认同",m),("自信表达",a)]
        strong = []
        weak = []
        for name, s in score_list:
            if s >=7:
                strong.append(name)
            if s <=4:
                weak.append(name)
        comment_text = ""
        if len(strong) > 0:
            comment_text += f"优势行为：{','.join(strong)}。在本次乡土文化符号校本课程实践中，该生在以上品质行为维度表现突出，在本土文化探究活动中展现良好素养。"
        if len(weak) >0:
            comment_text += f"待提升行为：{','.join(weak)}。后续乡土实践课程中，可以针对性引导，持续培育该生相关品质行为。"
        if not strong and not weak:
            comment_text = "各项品质行为表现均衡稳定，可继续在乡土文化实践活动中持续成长，深化对家乡本土文化符号的理解。"
        return comment_text

    if "student_df" not in st.session_state:
        st.session_state.student_df = pd.DataFrame(columns=["姓名","班级","共情感恩","专注坚持","协作互助","乡土认同","自信表达","个性化行为评语"])

    tab1, tab2 = st.tabs(["📥 批量上传全班表格","✍️ 手动新增单个学生"])

    with tab1:
        st.subheader("上传全班Excel/CSV行为记录表")
        st.write("表格表头：姓名,班级,共情感恩,专注坚持,协作互助,乡土认同,自信表达")
        upload_file = st.file_uploader("上传文件", type=["xlsx","csv"])
        if upload_file is not None:
            try:
                if upload_file.name.endswith(".csv"):
                    df_raw = pd.read_csv(upload_file)
                else:
                    df_raw = pd.read_excel(upload_file)
                df_raw["个性化行为评语"] = df_raw.apply(lambda row: generate_comment(row["共情感恩"],row["专注坚持"],row["协作互助"],row["乡土认同"],row["自信表达"]), axis=1)
                st.session_state.student_df = df_raw
                st.success("✅ 文件上传成功，自动生成学生品质行为评语")
                st.dataframe(df_raw, use_container_width=True)
            except Exception as err:
                st.error(f"读取文件失败，请检查表头：{err}")

    with tab2:
        st.subheader("手动录入单个学生课堂行为记录")
        colA, colB = st.columns(2)
        with colA:
            s_name = st.text_input("学生姓名")
            s_class = st.text_input("班级（例：301）")
            s_p = st.slider("共情感恩",0.0,10.0,5.0,0.1)
            s_e = st.slider("专注坚持",0.0,10.0,5.0,0.1)
        with colB:
            s_r = st.slider("协作互助",0.0,10.0,5.0,0.1)
            s_m = st.slider("乡土认同",0.0,10.0,5.0,0.1)
            s_a = st.slider("自信表达",0.0,10.0,5.0,0.1)
        if st.button("添加到全班成长档案"):
            new_comment = generate_comment(s_p,s_e,s_r,s_m,s_a)
            new_row = pd.DataFrame({
                "姓名":[s_name],
                "班级":[s_class],
                "共情感恩":[s_p],
                "专注坚持":[s_e],
                "协作互助":[s_r],
                "乡土认同":[s_m],
                "自信表达":[s_a],
                "个性化行为评语":[new_comment]
            })
            st.session_state.student_df = pd.concat([st.session_state.student_df, new_row], ignore_index=True)
            st.success("✅ 学生行为档案已添加")

    st.divider()
    st.subheader("全班品质行为档案预览 & 一键导出")
    st.dataframe(st.session_state.student_df, use_container_width=True)

    def export_excel(df):
        out = BytesIO()
        with pd.ExcelWriter(out, engine="openpyxl") as writer:
            df.to_excel(writer, index=False, sheet_name="学生品质行为成长档案")
        return out.getvalue()

    if not st.session_state.student_df.empty:
        excel_data = export_excel(st.session_state.student_df)
        st.download_button(
            label="📥 一键下载全班品质行为档案Excel",
            data=excel_data,
            file_name="学生品质行为成长档案.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
    st.markdown("</div>", unsafe_allow_html=True)
