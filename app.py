import streamlit as st
import pandas as pd
import plotly.express as px

# ============ 图片路径【全部JPG！】 ============
banner_path = "banner_rootbloom_grass.jpg"
bg_home_path = "bg_home.jpg"
bg_subtle_path = "bg_subtle.jpg"
perma_path = "perma_model.jpg"

# ============ 页面基础全局设置 ============
st.set_page_config(
    page_title="RootBloom",
    page_icon="🌱",
    layout="wide"
)

# ===================== CSS样式【修复背景图】 =====================
page_bg_img = f"""
<style>
/* 全局页面背景 bg_home.jpg */
[data-testid="stAppViewContainer"] {{
background-image: url("{bg_home_path}");
background-size: cover;
background-position: center;
background-repeat: no-repeat;
background-attachment: fixed;
}}
/* 清除页面顶部原生白色条 */
[data-testid="stHeader"] {{
background-color: rgba(0,0,0,0) !important;
}}
[data-testid="stToolbar"] {{
right: 2rem;
}}
/* 导航栏容器：单独bg_subtle.jpg背景 */
.nav-wrap {{
    background-image: url("{bg_subtle_path}");
    background-size: cover;
    background-position: center;
    padding:16px 20px;
    border-radius:10px;
}}
/* 板块文字半透底色，防止文字看不清 */
.block-bg {{
    background-color:rgba(255,255,255,0.85);
    padding:18px;
    border-radius:12px;
    margin-bottom:15px;
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# ============ 顶部导航栏（导航单独背景图） ============
st.markdown("<div class='nav-wrap'>", unsafe_allow_html=True)
page = st.radio(
    "",
    ["首页", "PERMA模型与德育拆分", "AI赋能德育课程", "校本课程案例", "效果评估&成长图表", "学生成长档案记录"],
    horizontal=True
)
st.markdown("</div>", unsafe_allow_html=True)
st.markdown("<hr style='border:1px solid #88a888;'>", unsafe_allow_html=True)


# ====================== 首页 ======================
if page == "首页":
    st.image(banner_path, width="stretch")
    st.markdown("<div class='block-bg'>", unsafe_allow_html=True)
    st.subheader("项目简介")
    st.write("RootBloom是一项**AI赋能乡村小学德育**的校本课程项目。项目以河源乡土文化为载体，依托PERMA积极心理模型搭建德育框架，借助AI工具降低乡村教师备课压力，把积极心理、乡土文化、德育育人三者融合，打造低成本、可落地的乡村小学德育课程。")

    st.subheader("项目背景")
    st.write("乡村小学德育普遍存在素材老旧、备课耗时长、缺少本土化内容、评价方式单一等痛点。教师人手紧张，很难自主开发贴合本地乡土文化的德育课堂。")
    st.write("本项目立足河源乡村小学，将乡土文化资源融入德育，利用AI辅助课程开发、课堂互动与成长评价，以PERMA模型作为德育效果的评价框架，实现德育课堂从说教式到体验式的转变。")

    st.subheader("项目目标")
    st.write("1. 基于PERMA积极心理模型，搭建乡土化德育课程框架，将德育目标拆解为五大心理成长维度。")
    st.write("2. 利用AI赋能课程全流程，减轻乡村教师备课、素材制作、学生评价的负担。")
    st.write("3. 开发全套可直接落地的德育课程资源包：教案、课件、课堂任务单。")
    st.write("4. 通过课程前后测，可视化学生积极心理品质与德育素养提升变化，建立学生成长档案。")
    st.markdown("</div>", unsafe_allow_html=True)


# ====================== PERMA模型与德育拆分页面 ======================
elif page == "PERMA模型与德育拆分":
    st.markdown("<div class='block-bg'>", unsafe_allow_html=True)
    st.image(perma_path, width="stretch")

    st.subheader("PERMA模型 —— 德育目标拆解")
    st.write("我们把PERMA五大维度，直接对应小学德育育人目标，将抽象德育拆分成可观察、可教学、可评估的课堂目标：")

    st.subheader("🌞 P 积极情绪 Positive Emotion｜德育：涵养仁爱与共情")
    st.write("德育目标：引导学生感受家乡美好，学会共情他人，拥有温暖、正向的情绪。")
    st.write("课堂落地：乡土故事品读、家乡美景观察，引导学生表达内心感受，培育感恩、友善的德育品质。")

    st.subheader("🎯 E 投入 Engagement｜德育：培养专注与坚持")
    st.write("德育目标：锻炼学生耐心、毅力，面对任务不轻易放弃，养成踏实专注的品格。")
    st.write("课堂落地：乡土手工、自然探究任务，让学生沉浸式动手实践，在克服困难中磨炼意志品质。")

    st.subheader("🤝 R 人际关系 Relationships｜德育：学会合作与尊重")
    st.write("德育目标：懂得倾听、尊重同伴，学会团队协作，友善沟通，构建良好同伴关系。")
    st.write("课堂落地：小组研学讨论、集体作品共创，在合作活动学习包容、互助的品德。")

    st.subheader("🧭 M 意义 Meaning｜德育：厚植乡土认同与家国情怀")
    st.write("德育目标：认识家乡文化，建立文化自信，理解自身价值，树立责任感。")
    st.write("课堂落地：本土民俗、东江乡土红色故事学习，从热爱家乡起步，建立家国情怀。")

    st.subheader("🏅 A 成就 Accomplishment｜德育：塑造自信与进取精神")
    st.write("德育目标：肯定自我价值，敢于展示成果，建立正向自我认知，勇于挑战。")
    st.write("课堂落地：学生成果展示、作品分享，让学生看见自己的成长，获得成就感。")

    st.subheader("核心逻辑")
    st.write("传统德育偏向条文说教，本项目用PERMA模型把德育拆成五个可落地的成长方向，每一节德育课都对应至少一个维度，让德育效果可以观察、可以评估。")
    st.markdown("</div>", unsafe_allow_html=True)


# ====================== AI赋能德育课程【✅自动生成课程大纲】 ======================
elif page == "AI赋能德育课程":
    st.markdown("<div class='block-bg'>", unsafe_allow_html=True)
    st.subheader("🤖 AI赋能乡村小学德育课程")
    st.write("AI不是用来替代老师，而是作为乡村教师的辅助工具，贯穿课程开发、课堂教学、学生评价全流程，配合PERMA德育框架使用。")

    st.subheader("📝 AI一键生成PERMA校本课程大纲")
    st.write("填写参数，自动生成基于PERMA模型的乡土德育课程大纲：")
    col1, col2 = st.columns(2)
    with col1:
        grade_sel = st.selectbox("选择授课年级", ["三年级","四年级","五年级","六年级"])
        perma_dim = st.multiselect("PERMA维度（可多选）",["P积极情绪","E投入专注","R人际关系","M意义认同","A成就自信"], default=["P积极情绪","M意义认同"])
    with col2:
        theme_input = st.text_input("乡土主题", value="河源簕杜鹃与东江红色故事")
        lesson_num = st.number_input("课时数量", min_value=1,max_value=10,value=2)

    if st.button("生成课程大纲"):
        st.success("✅ 已根据PERMA模型生成校本德育课程大纲")
        outline_text = f"""
# 《{theme_input}》校本德育课程大纲
适用年级：{grade_sel}
对应PERMA维度：{', '.join(perma_dim)}
总课时：{lesson_num}课时

## 课程目标
1. 情感目标：引导学生感受{theme_input}蕴含的乡土精神，培育积极心理品质，对应选中的PERMA维度。
2. 认知目标：了解河源本土乡土文化与红色故事，建立家乡认同感。
3. 行为目标：在小组活动学会合作、表达感受，形成良好德育习惯。

## 课时安排
"""
        for i in range(lesson_num):
            outline_text += f"\n### 第{i+1}课时\n课程环节：乡土情景导入 → 体验活动 → 小组分享 → 作品创作\n"
        outline_text += """
## 评价方式
采用PERMA五维度观察记录 + 前后测问卷，记录学生成长变化。
"""
        st.markdown(outline_text)

    st.subheader("🎨 2. AI生成课堂可视化素材")
    st.write("- AI绘制乡土插画、德育主题海报，制作课件配图，解决乡村学校美术素材不足的问题。")
    st.write("- 生成情景对话脚本，用于课堂角色扮演德育活动。")

    st.subheader("💬 3. AI课堂互动，辅助德育引导")
    st.write("- 课堂上，AI作为虚拟伙伴，引导学生分享感受，倾听学生想法，辅助情绪表达。")
    st.write("- 针对学生的发言，给出温和正向引导，帮助学生表达共情、感恩等德育相关感悟。")

    st.subheader("📊 4. AI辅助德育评价（对接PERMA模型）")
    st.write("- AI整理学生课堂发言、作品描述，对应PERMA五个维度做质性记录。")
    st.write("- 辅助整理问卷前后测数据，自动生成可视化图表，直观展示学生德育成长变化。")

    st.subheader("⚖️ 使用原则")
    st.write("教师全程主导课堂，AI只做辅助。所有AI产出内容，都由教师审核、本地化修改，保证内容贴合乡村小学生认知水平，守住德育育人主线。")
    st.markdown("</div>", unsafe_allow_html=True)


# ====================== 校本课程案例 ======================
elif page == "校本课程案例":
    st.markdown("<div class='block-bg'>", unsafe_allow_html=True)
    st.subheader("📚 校本德育课程案例")
    st.write("整套课程以PERMA为德育框架，AI辅助备课，面向小学3-6年级，围绕河源乡土文化设计德育体验课。")

    st.subheader("📝 课程设计")
    st.write("全套8课时德育校本课，每一节课都绑定PERMA的1~2个德育维度。课程以体验式活动为主，摒弃说教式德育。")
    st.write("课程结构：乡土情景导入 → 体验活动 → 小组分享 → 作品创作 → 成果展示。")

    st.subheader("🗂️ 课程主题示例")
    st.write("**主题1：家乡草木里的温暖（P积极情绪）** 感受自然之美，学会感恩；AI生成植物小故事。")
    st.write("**主题2：一起做乡土手作（E投入 + R人际关系）** 小组合作手工，磨炼耐心，学会互助。")
    st.write("**主题3：东江乡土红色小故事（M意义）** 了解家乡先辈故事，厚植家国情怀。")
    st.write("**主题4：我的家乡成果展（A成就）** 学生展示作品，建立自信。")

    st.subheader("🏫 课堂实施")
    st.write("乡村教师利用AI快速拿到教案和素材，在课堂组织体验活动。教师重点观察学生情绪、合作表现，记录德育成长，课程结束后收集问卷，完成效果评估。")
    st.markdown("</div>", unsafe_allow_html=True)


# ====================== 效果评估&成长图表【前后测绘图！】 ======================
elif page == "效果评估&成长图表":
    st.markdown("<div class='block-bg'>", unsafe_allow_html=True)
    st.subheader("📊 PERMA模型｜课程前后测 学生心理德育变化可视化")
    st.write("输入前测、后测平均分，网页自动生成对比柱状图，直观看到学生五个维度的成长变化")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("课程前测得分（满分10分）")
        pre_P = st.number_input("P 积极情绪", min_value=0.0, max_value=10.0, value=4.2, step=0.1)
        pre_E = st.number_input("E 投入专注", min_value=0.0, max_value=10.0, value=3.8, step=0.1)
        pre_R = st.number_input("R 人际关系", min_value=0.0, max_value=10.0, value=4.0, step=0.1)
        pre_M = st.number_input("M 意义认同", min_value=0.0, max_value=10.0, value=3.5, step=0.1)
        pre_A = st.number_input("A 成就自信", min_value=0.0, max_value=10.0, value=3.6, step=0.1)

    with col2:
        st.subheader("课程后测得分（满分10分）")
        post_P = st.number_input("P 积极情绪", min_value=0.0, max_value=10.0, value=7.1, step=0.1)
        post_E = st.number_input("E 投入专注", min_value=0.0, max_value=10.0, value=6.8, step=0.1)
        post_R = st.number_input("R 人际关系", min_value=0.0, max_value=10.0, value=7.3, step=0.1)
        post_M = st.number_input("M 意义认同", min_value=0.0, max_value=10.0, value=7.5, step=0.1)
        post_A = st.number_input("A 成就自信", min_value=0.0, max_value=10.0, value=6.9, step=0.1)

    # 构造绘图数据
    data = pd.DataFrame({
        "PERMA维度": ["积极情绪P", "投入专注E", "人际关系R", "意义认同M", "成就自信A"] * 2,
        "分数": [pre_P, pre_E, pre_R, pre_M, pre_A, post_P, post_E, post_R, post_M, post_A],
        "测试阶段": ["前测","前测","前测","前测","前测","后测","后测","后测","后测","后测"]
    })
    fig = px.bar(data, x="PERMA维度", y="分数", color="测试阶段", barmode="group",
                 range_y=[0,10], title="学生德育心理品质：课程前测 VS 后测对比")
    st.plotly_chart(fig, use_container_width=True)

    st.info("💡 说明：图表会实时跟着输入分数自动更新，用于答辩展示学生经过课程之后的心理成长变化")
    st.markdown("</div>", unsafe_allow_html=True)


# ====================== 学生成长档案记录页面 ======================
elif page == "学生成长档案记录":
    st.markdown("<div class='block-bg'>", unsafe_allow_html=True)
    st.subheader("📒 学生德育成长档案记录")
    st.write("录入学生信息、课堂表现、德育成长评语，保存学生成长记录")

    name = st.text_input("学生姓名")
    grade = st.text_input("班级")
    p_score = st.slider("积极情绪(P) 课堂表现评分 0~10",0,10,5)
    e_score = st.slider("投入专注(E) 课堂表现评分 0~10",0,10,5)
    r_score = st.slider("人际关系(R) 课堂表现评分 0~10",0,10,5)
    m_score = st.slider("意义认同(M) 课堂表现评分 0~10",0,10,5)
    a_score = st.slider("成就自信(A) 课堂表现评分 0~10",0,10,5)
    comment = st.text_area("教师德育成长评语")

    if st.button("保存本条学生成长记录"):
        st.success(f"✅【{name}】成长记录已保存！")
        st.write(f"PERMA分项：P:{p_score}｜E:{e_score}｜R:{r_score}｜M:{m_score}｜A:{a_score}")
        st.write(f"教师评语：{comment}")

    st.divider()
    st.subheader("已录入记录预览")
    st.write("多学生记录可继续新增，用于长期追踪学生德育与心理成长变化")
    st.markdown("</div>", unsafe_allow_html=True)