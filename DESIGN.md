---
name: 故事繪本
description: 給國小低年級的離線互動故事繪本，像一本放在床邊、會輕輕動的精裝書
colors:
  cloth: "#2e5e8c"
  cloth-deep: "#1f4468"
  cloth-hover: "#2f4577"
  marigold: "#f2c14e"
  marigold-deep: "#e3a92f"
  tomato: "#e9573f"
  tomato-deep: "#8e2a22"
  kiku: "#f2b000"
  kiku-pale: "#ffe08a"
  leaf: "#7cb26a"
  leaf-deep: "#3d7a35"
  rose: "#d9667a"
  page: "#fffdf8"
  page-edge: "#ece5d6"
  ink: "#263042"
  ink-soft: "#55607a"
  wood: "#b9773f"
  wood-light: "#d39457"
  wood-deep: "#8a5228"
  wood-back: "#6e4323"
typography:
  display:
    fontFamily: "ZhuyinKai, BiauKai, DFKai-SB, Kaiti TC, serif"
    fontSize: "clamp(42px, min(10vmin, 15cqi), 120px)"
    fontWeight: 400
    lineHeight: 1.15
  headline:
    fontFamily: "ZhuyinKai, BiauKai, DFKai-SB, Kaiti TC, serif"
    fontSize: "clamp(34px, 5.6vmin, 68px)"
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: "0.02em"
  body:
    fontFamily: "ZhuyinKai, BiauKai, DFKai-SB, Kaiti TC, serif"
    fontSize: "clamp(24px, 4vmin, 44px)"
    fontWeight: 400
    lineHeight: 1.6
  label:
    fontFamily: "ZhuyinKai, BiauKai, DFKai-SB, Kaiti TC, serif"
    fontSize: "clamp(20px, 3vmin, 32px)"
    fontWeight: 400
    lineHeight: 1.2
  folio:
    fontFamily: "ZhuyinKai, BiauKai, DFKai-SB, Kaiti TC, serif"
    fontSize: "clamp(15px, 2vmin, 20px)"
    fontWeight: 400
rounded:
  page: "3px"
  art: "8px"
  cover: "10px"
  button: "12px"
  nav: "14px"
  pill: "999px"
spacing:
  step: "clamp(10px, 1.6vmin, 20px)"
  board: "clamp(14px, 2vmin, 20px)"
  page-x: "clamp(22px, 4vmin, 52px)"
  page-y: "clamp(20px, 3.6vmin, 44px)"
components:
  nav-next:
    backgroundColor: "{colors.cloth}"
    textColor: "{colors.page}"
    typography: "{typography.label}"
    rounded: "{rounded.nav}"
    height: "clamp(66px, 10vmin, 92px)"
    width: "clamp(170px, 24vmin, 260px)"
  nav-next-hover:
    backgroundColor: "{colors.cloth-hover}"
  nav-prev:
    backgroundColor: "{colors.page}"
    textColor: "{colors.cloth}"
    rounded: "{rounded.nav}"
    height: "clamp(66px, 10vmin, 92px)"
  nav-home:
    backgroundColor: "{colors.page}"
    textColor: "{colors.cloth}"
    rounded: "{rounded.nav}"
  button-cloth:
    backgroundColor: "{colors.cloth}"
    textColor: "{colors.page}"
    typography: "{typography.label}"
    rounded: "{rounded.button}"
    padding: "0.45em 1em"
    height: "64px"
  index-tab:
    backgroundColor: "{colors.page}"
    textColor: "{colors.ink}"
    rounded: "{rounded.button}"
  index-tab-passed:
    backgroundColor: "{colors.cloth}"
    textColor: "{colors.page}"
  index-tab-here:
    backgroundColor: "{colors.tomato}"
    textColor: "#ffffff"
  shelf-tab:
    backgroundColor: "{colors.page}"
    textColor: "{colors.wood-back}"
    rounded: "{rounded.pill}"
    height: "clamp(56px, 8.4vmin, 80px)"
  shelf-tab-selected:
    backgroundColor: "{colors.wood-deep}"
    textColor: "{colors.page}"
---

# Design System: 故事繪本

## Overview

**Creative North Star: "床邊的精裝繪本"**

整套書要像一本放在床邊、會輕輕動的精裝繪本。螢幕上看到的是一個實體物件：布面書衣包著一疊米白紙頁，中間有書溝的陰影，右邊有索引籤，翻頁時紙張會真的轉過去。數位的部分只做兩件事：讓翻書更順手，讓畫面裡的東西被點到時輕輕回應。介面盡量退到後面，故事和插畫才是主角。

質感來自克制。每本書只有一個布面主色加上一個蝴蝶頁底色，其餘都是紙色和墨藍字。字體全書只用注音楷體，靠字級和顏色分層次。動作慢而柔，收尾用長緩出曲線。小朋友看到的是溫暖、熟悉、像課本又比課本好看的書，沒有遊戲介面那種催促感。

同一份頁面要在兩種距離下成立：教室投影時，最後一排也讀得到；平板上，小手也點得準。所以字級和觸控目標都用 `vmin` 和 `clamp()` 跟著螢幕縮放，直向螢幕改成單頁，圖在上、字在下。

**Key Characteristics:**
- 實體書的隱喻：布面書衣、紙頁疊層、書溝、索引籤、3D 翻頁。
- 每本書一套「布色＋蝴蝶頁色＋強調色」，其他設計語言全系列共用。
- 全書注音楷體，不混用第二套字體。
- 互動只用來發現、推動劇情，從不評分、從不懲罰。
- 動作柔和緩慢，完整支援 `prefers-reduced-motion`。

## Colors

整體是低彩度的暖色：米白紙頁、墨藍字，再加上每本書自己的一組節慶色。

### Primary
- **布面書衣色**（cloth，書櫃預設 #2e5e8c 靛藍布）：書衣、「下一頁」按鈕、已讀過的索引籤、對話文字（`.say`）、副標題。**每本書會改成自己的顏色**：春節朱紅布 #a52a24、中秋夜藍布 #24365e、端午艾草綠 #3d7a35、七夕紫藤布 #5b4a8a、土地公泥土棕 #7a5a3a……
- **深布色**（cloth-deep）：書衣底緣厚度、鍵盤焦點外框。
- **布面滑過色**（cloth-hover）：布面按鈕滑過時的顏色。

### Secondary
- **蝴蝶頁底色**（marigold，書櫃預設 #f2c14e 金盞黃）：書以外的整片背景，上面鋪一層同色系、更深一階（marigold-deep）的小圖紋，像精裝書的蝴蝶頁。每本書會換成配合故事的顏色，例如端午用湖水青、日月潭用潭水藍。

### Tertiary
- **目前頁標記色**（tomato，書櫃預設 #e9573f 番茄紅）：只用在「目前這一頁」的索引籤。深一階的 tomato-deep 用在互動提示文字（`.hint`）。如果布色本身就是紅色系（例如媽祖、灶神），就改用藍色或綠色當標記色，和布色拉開。

### Neutral
- **米白紙頁**（page #fffdf8）：所有書頁、淺色按鈕底。全系列不用純白當紙。
- **紙緣**（page-edge #ece5d6）：紙頁疊層的線條、插圖相框外圈、淺色按鈕內框。
- **墨藍字**（ink #263042）：內文與標題。全系列不用純黑。
- **淡墨字**（ink-soft #55607a）：頁碼。
- **木頭四色**（wood、wood-light、wood-deep、wood-back）：只用在首頁書櫃的櫃體、層板、櫃內陰影。
- **插畫點綴色**（kiku 菊黃、leaf 葉綠、rose 玫瑰粉）：插圖和撒花效果用的共用顏色。

### Named Rules
**The One Cloth Rule.** 一本書只有一個布色當主角，所有「可以按」和「書的身分」都用這個顏色。換一本書，換掉的就是這組顏色，版面語言不變。

**The Paper-Not-White Rule.** 紙一律用米白（page），字一律用墨藍（ink）。純白只出現在插圖相框內圈和紙頁疊層的亮線。

**The Quiet Saturation Rule.** 節慶色要降一點彩度，不用螢光色、彩虹配色，也不用大面積的高飽和紅。

## Typography

**Display / Body / Label Font:** 字咍注音標楷（ZhuyinKai，退回 BiauKai、DFKai-SB、Kaiti TC、serif）

**Character:** 楷體加注音，是低年級課本最熟悉的字感，讓人有安全感，也帶一點書卷氣。全書只用這一套，字重固定是 400。

### Hierarchy
- **Display**（400，clamp(42px, min(10vmin, 15cqi), 120px)，1.15）：封面書名。副標用 0.5em，顏色是布色。
- **Headline**（400，clamp(34px, 5.6vmin, 68px)，1.25，0.02em）：頁面標題、首頁「故事繪本」。用 `text-wrap: balance`。
- **Body**（400，clamp(24px, 4vmin, 44px)，1.6）：故事內文，一頁 2～3 句。直向螢幕時改成 clamp(20px, 3.4vw, 38px)，行高 1.5。
- **Label**（400，clamp(20px, 3vmin, 32px)，1.2～1.3）：按鈕、互動提示。導覽鈕再大一號，clamp(24px, 3.8vmin, 40px)。
- **Folio**（400，clamp(15px, 2vmin, 20px)）：頁碼，用淡墨色，置中放在頁底。

### Named Rules
**The One Typeface Rule.** 不加圓體、黑體或卡通字型。層次只靠字級和顏色。

**The Unbroken Phrase Rule.** 詞語不能被拆在兩行，必要時用 `.w`（nowrap）包住。破音字一律在來源用「字[注音]」標記。

## Layout

- **橫向（寬 > 高）**：一本攤開的書，左右兩頁並排（`grid-template-columns: 1fr 1fr`）。通常一頁放插圖、一頁放文字。索引籤垂直排在書的右側外緣，上一頁／回書櫃／下一頁三顆按鈕排在書下方。
- **直向（`max-aspect-ratio: 1/1`）**：改成單頁，插圖和文字上下排（56fr／44fr），翻頁動畫改成單頁版本，書溝陰影隱藏。
- **節奏**：基本間距 step 是 clamp(10px, 1.6vmin, 20px)。書衣到紙頁的厚度 board 是 clamp(14px, 2vmin, 20px)。頁內留白左右 page-x、上下 page-y。
- **插圖**：固定 4:3，用 container query 在可用空間裡盡量放大。
- **首頁書櫃**：木頭櫃，層數依螢幕和書的數量動態計算。書是 3:4 的封面朝外擺放，旁邊有裝飾用的書背和盆栽。上方用分頁切換「節日故事／台灣故事」。
- 全頁不捲動（`overflow: hidden`），一個畫面就是一個跨頁。

## Elevation & Depth

用陰影表現**實體物件的厚度**，不是拿來排 UI 的層級。陰影一律帶暖棕色調（`rgba(80, 50, 10, .45)`），不用冷灰。

### Shadow Vocabulary
- **書本落地影**（`0 30px 44px -24px rgba(60,35,5,.65)`）：整本書和書櫃放在桌上的影子。
- **書衣厚度**（`0 4px 0 var(--cloth-deep)` 加內側 `inset 0 0 18px rgba(10,30,55,.35)`）：布面的邊緣與暗角。
- **紙頁疊層**（多層 1px 的 page-edge／白色交錯 box-shadow）：書頁底部看得到一疊紙。
- **書溝**（中央 120px 的線性漸層）：左右兩頁中間的凹陷與反光。
- **按鈕浮起**（`0 12px 18px -12px var(--shadow)`）：按鈕像一張微微浮起的卡紙，按下時往下移 3px，陰影跟著縮小。
- **插圖相框**（`0 0 0 6px #fff, 0 0 0 7px var(--page-edge), 0 16px 24px -12px var(--shadow)`）：像貼在書頁上的一張圖。

### Named Rules
**The Physical Object Rule.** 每個陰影都要說得出它對應實體書的哪個部分。說不出來，就不要加。

## Shapes

形狀語言照實體書來：紙頁幾乎是直角（3px），插圖相框 8px，書衣 10px，布面按鈕和索引籤 12px，導覽鈕 14px。只有首頁的分類分頁用整顆圓角（999px），像兩顆藥丸按鈕。索引籤只有右邊有圓角（`0 12px 12px 0`），像從書頁邊緣伸出去的紙籤。插畫角色用圓潤的幾何造形，以色塊分形狀。

## Components

### 導覽按鈕（上一頁／下一頁／回書櫃）
厚實、好按、溫和。
- **Shape:** 柔和圓角（14px），高 clamp(66px, 10vmin, 92px)，最小寬 clamp(170px, 24vmin, 260px)，在投影和平板上都夠大。
- **下一頁:** 布色底、紙色字，箭頭是圓頭線條 SVG（stroke 3.2）。
- **上一頁／回書櫃:** 紙色底、布色字，有 3px 的布色內框。第一頁的「上一頁」用 `visibility: hidden` 保留位置，版面才不會跳動。
- **States:** 滑過換 cloth-hover；按下往下 3px；焦點是 4px 深布色外框。

### 布面按鈕（頁內互動按鈕）
- 布色底、紙色字、12px 圓角，最小高度 64px。按下往下 3px。

### 索引籤
- 從書頁右緣伸出去的紙籤，平分書的高度。三種狀態：**還沒讀到**（紙色）、**讀過了**（布色）、**目前這頁**（標記色，往外推 14px）。滑過時往外推 6px。

### 首頁分類分頁
- 藥丸形，紙色底、木色字，有木色內框。選到的那個改成深木色底、紙色字。

### 封面朝外的繪本（首頁）
- 3:4 布面書衣，有細格紋、書背折痕，書口露出紙頁。中間貼一張紙色書名標籤，外框是該書的強調色。滑過時微微抬起、傾斜 1.5°；點下去先放大，再進入那本書。

### 可點的插圖（`[data-act]`）
這套書的招牌元件。
- 插圖裡可以點的角色或物件，被點到時播一次 `.bump` 動畫（wobble、hop、shake，0.7～0.8 秒）。整頁完成後加上 `.done`，觸發移動（`.mover`）、淡入（`.show-done`）、祝福語（`.cheer`）和撒花。
- 提示文字（`.hint`）在完成前後切換兩段文字，用 tomato-deep 色。
- SVG 裡的按鈕有 `role="button"` 和鍵盤焦點外框。

## Do's and Don'ts

### Do:
- **Do** 每本新書只換「布色＋蝴蝶頁色＋標記色＋蝴蝶頁圖紋」，翻頁、索引籤、導覽鈕、字體都沿用。
- **Do** 字級和觸控目標都用 `clamp()` 加 `vmin`，觸控目標最小 56px，主要導覽 66px 以上。
- **Do** 動作用 `--ease`（cubic-bezier(0.16, 1, 0.3, 1)），時間 0.25～1 秒；所有動畫都要被 `prefers-reduced-motion` 關掉。
- **Do** 一頁最多 2～3 句。插圖面積比文字大。
- **Do** 互動要給劇情回饋：點了角色會動、東西會出現。完成整頁才出現祝福語或撒花。
- **Do** 預留朗讀語音的位置：每頁文字是完整句子，翻頁和互動不能只靠讀懂文字才能完成。
- **Do** 插畫角色用圓潤幾何造形，臉部簡單（點點眼、小腮紅），以色塊分形狀。

### Don't:
- **Don't** 出現計分、倒數、星星評等、紅色叉叉，或任何「答錯了」的回饋。
- **Don't** 加日曆、由來說明、問答這類教學頁。
- **Don't** 用純黑字、純白紙、螢光色或彩虹配色。
- **Don't** 混用第二套字體，也不要用粗體做強調。
- **Don't** 用彈跳過頭、閃爍、快速循環的動畫。持續的動畫只能是很慢的飄、閃（1.2 秒以上，來回交替）。
- **Don't** 加裝飾用的亮片、星星邊框、花紋框線，畫面要留白。
- **Don't** 畫大眼萌系角色。
