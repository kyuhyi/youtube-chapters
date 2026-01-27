# 🤖 Clawdbot 완벽 설치 가이드

> 핸드폰으로 PC를 조종하고 개발까지 시키는 AI 비서 설치하기

---

## 📋 목차

1. [사전 준비](#1-사전-준비)
2. [Node.js 설치](#2-nodejs-설치)
3. [Clawdbot 설치](#3-clawdbot-설치)
4. [Anthropic API 키 발급](#4-anthropic-api-키-발급)
5. [Clawdbot 초기 설정](#5-clawdbot-초기-설정)
6. [텔레그램 연동](#6-텔레그램-연동)
7. [슬랙 연동](#7-슬랙-연동)
8. [브라우저 확장 프로그램 설치](#8-브라우저-확장-프로그램-설치)
9. [테스트하기](#9-테스트하기)
10. [문제 해결](#10-문제-해결)

---

## 1. 사전 준비

### 필요한 것들
- ✅ Windows 10/11 또는 macOS (Apple Silicon/Intel 모두 지원)
- ✅ 인터넷 연결
- ✅ Anthropic 계정 (Claude API 사용)
- ✅ 텔레그램 또는 슬랙 계정

### 예상 소요 시간
- 약 15-20분

---

## 2. Node.js 설치

Clawdbot은 Node.js로 만들어졌기 때문에 먼저 Node.js를 설치해야 합니다.

### Windows

1. **Node.js 공식 사이트 접속**
   - https://nodejs.org/ko 접속
   
2. **LTS 버전 다운로드**
   - 왼쪽 초록색 버튼 **"LTS"** 클릭 (예: 22.x.x LTS)
   - ⚠️ "최신 버전" 말고 반드시 **LTS** 선택!

3. **설치 진행**
   - 다운로드된 `.msi` 파일 실행
   - "Next" 계속 클릭
   - ✅ **"Automatically install the necessary tools"** 체크 (중요!)
   - "Install" 클릭

4. **설치 확인**
   - `Win + R` → `cmd` 입력 → 엔터
   - 아래 명령어 입력:
   ```bash
   node -v
   ```
   - `v22.x.x` 같은 버전이 나오면 성공!

### macOS

1. **터미널 열기**
   - `Cmd + Space` → "터미널" 검색 → 실행

2. **Homebrew 설치** (없는 경우)
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

3. **Node.js 설치**
   ```bash
   brew install node
   ```

4. **설치 확인**
   ```bash
   node -v
   ```

---

## 3. Clawdbot 설치

### Windows (PowerShell 관리자 권한)

1. **PowerShell 관리자 권한으로 실행**
   - 시작 버튼 우클릭 → "Windows PowerShell (관리자)" 또는 "터미널 (관리자)"

2. **Clawdbot 설치**
   ```powershell
   npm install -g clawdbot
   ```

3. **설치 확인**
   ```powershell
   clawdbot --version
   ```

### macOS

1. **터미널에서 설치**
   ```bash
   npm install -g clawdbot
   ```

2. **설치 확인**
   ```bash
   clawdbot --version
   ```

---

## 4. Anthropic API 키 발급

Clawdbot은 Claude AI를 사용하므로 Anthropic API 키가 필요합니다.

1. **Anthropic Console 접속**
   - https://console.anthropic.com 접속
   - 계정이 없으면 회원가입

2. **API Keys 메뉴 이동**
   - 좌측 메뉴에서 **"API Keys"** 클릭

3. **새 키 생성**
   - **"Create Key"** 버튼 클릭
   - 이름 입력 (예: "clawdbot")
   - **"Create Key"** 클릭

4. **키 복사 & 저장**
   - 생성된 키 복사 (sk-ant-api03-... 형태)
   - ⚠️ **이 키는 다시 볼 수 없으니 반드시 어딘가에 저장!**

5. **결제 수단 등록** (필수)
   - 좌측 메뉴 **"Plans & Billing"** → **"Payment Methods"**
   - 신용카드 등록
   - ⚠️ 카드 등록 안 하면 API 호출 안 됨!

---

## 5. Clawdbot 초기 설정

### 작업 폴더 생성 및 이동

```bash
# Windows (PowerShell)
mkdir C:\Users\%USERNAME%\clawd
cd C:\Users\%USERNAME%\clawd

# macOS
mkdir ~/clawd
cd ~/clawd
```

### Clawdbot 초기화

```bash
clawdbot init
```

이 명령어를 실행하면 설정 마법사가 시작됩니다:

1. **Anthropic API Key 입력**
   - 아까 복사한 API 키 붙여넣기

2. **기본 모델 선택**
   - `claude-sonnet-4-20250514` 권장 (성능/비용 균형)
   - 또는 `claude-opus-4-20250514` (최고 성능, 비용 높음)

3. **작업 디렉토리 설정**
   - 기본값 사용 (엔터)

### 설정 파일 확인

```bash
# 설정 파일 위치
# Windows: C:\Users\사용자명\.clawdbot\config.yaml
# macOS: ~/.clawdbot/config.yaml
```

---

## 6. 텔레그램 연동

### 6-1. 텔레그램 봇 생성

1. **텔레그램 앱에서 BotFather 검색**
   - 텔레그램 앱 열기
   - 검색창에 `@BotFather` 입력
   - 파란 체크마크 있는 공식 계정 선택

2. **새 봇 생성**
   - `/newbot` 입력
   - 봇 이름 입력 (예: "나의 AI 비서")
   - 봇 username 입력 (예: `my_ai_assistant_bot`)
     - ⚠️ 반드시 `_bot`으로 끝나야 함!

3. **토큰 저장**
   - BotFather가 보내주는 토큰 복사
   - 형태: `1234567890:ABCdefGHIjklMNOpqrsTUVwxyz`

### 6-2. 내 텔레그램 Chat ID 확인

1. **@userinfobot 검색**
   - 텔레그램에서 `@userinfobot` 검색
   - 대화 시작

2. **Chat ID 확인**
   - 아무 메시지나 보내면 내 정보 표시
   - `Id: 123456789` ← 이 숫자가 Chat ID

### 6-3. Clawdbot에 텔레그램 설정

```bash
clawdbot config edit
```

설정 파일이 열리면 아래 내용 추가:

```yaml
channels:
  telegram:
    enabled: true
    token: "1234567890:ABCdefGHIjklMNOpqrsTUVwxyz"  # BotFather 토큰
    allowlist:
      - "123456789"  # 내 Chat ID
```

### 6-4. Clawdbot 재시작

```bash
clawdbot gateway restart
```

### 6-5. 테스트

1. 텔레그램에서 내가 만든 봇 검색
2. `/start` 입력
3. "안녕!" 메시지 보내기
4. 응답이 오면 성공! 🎉

---

## 7. 슬랙 연동

### 7-1. Slack App 생성

1. **Slack API 사이트 접속**
   - https://api.slack.com/apps 접속
   - Slack 계정으로 로그인

2. **Create New App 클릭**
   - **"From scratch"** 선택
   - App Name: `Clawdbot` (원하는 이름)
   - Workspace: 연결할 워크스페이스 선택
   - **"Create App"** 클릭

### 7-2. Bot Token 권한 설정

1. **OAuth & Permissions 메뉴 이동**
   - 좌측 메뉴에서 **"OAuth & Permissions"** 클릭

2. **Scopes 추가**
   - 스크롤 내려서 **"Bot Token Scopes"** 찾기
   - **"Add an OAuth Scope"** 클릭
   - 아래 권한들 모두 추가:
     ```
     app_mentions:read
     channels:history
     channels:read
     chat:write
     groups:history
     groups:read
     im:history
     im:read
     im:write
     users:read
     ```

3. **앱 설치**
   - 페이지 상단으로 스크롤
   - **"Install to Workspace"** 클릭
   - **"허용"** 클릭

4. **Bot Token 복사**
   - 설치 완료 후 **"Bot User OAuth Token"** 복사
   - 형태: `xoxb-여러숫자-여러숫자-영문자조합`

### 7-3. App-Level Token 생성

1. **Basic Information 메뉴 이동**
   - 좌측 메뉴에서 **"Basic Information"** 클릭

2. **App-Level Tokens 생성**
   - 스크롤 내려서 **"App-Level Tokens"** 찾기
   - **"Generate Token and Scopes"** 클릭
   - Token Name: `socket` (아무 이름)
   - **"Add Scope"** 클릭 → `connections:write` 추가
   - **"Generate"** 클릭
   - 토큰 복사 (형태: `xapp-숫자-영문자조합`)

### 7-4. Socket Mode 활성화

1. **Socket Mode 메뉴 이동**
   - 좌측 메뉴에서 **"Socket Mode"** 클릭

2. **Socket Mode 켜기**
   - **"Enable Socket Mode"** 토글 ON

### 7-5. Event Subscriptions 설정

1. **Event Subscriptions 메뉴 이동**
   - 좌측 메뉴에서 **"Event Subscriptions"** 클릭

2. **이벤트 활성화**
   - **"Enable Events"** 토글 ON

3. **Bot Events 추가**
   - **"Subscribe to bot events"** 펼치기
   - **"Add Bot User Event"** 클릭
   - 아래 이벤트들 추가:
     ```
     app_mention
     message.channels
     message.groups
     message.im
     ```

4. **저장**
   - 하단 **"Save Changes"** 클릭

### 7-6. Clawdbot에 슬랙 설정

```bash
clawdbot config edit
```

설정 파일에 아래 내용 추가:

```yaml
channels:
  slack:
    enabled: true
    botToken: "여기에-Bot-User-OAuth-Token-붙여넣기"
    appToken: "여기에-App-Level-Token-붙여넣기"
    allowlist:
      - "U01234ABCDE"                     # 허용할 사용자 ID
```

### 7-7. 내 Slack User ID 확인

1. Slack 앱에서 내 프로필 클릭
2. 프로필 보기
3. 더보기(⋯) → "멤버 ID 복사"
4. 이 ID를 allowlist에 추가

### 7-8. Clawdbot 재시작

```bash
clawdbot gateway restart
```

### 7-9. 테스트

1. Slack 워크스페이스에서 Clawdbot 앱과 DM 시작
2. "안녕!" 메시지 보내기
3. 응답이 오면 성공! 🎉

---

## 8. 브라우저 확장 프로그램 설치

Clawdbot이 브라우저를 제어할 수 있게 해주는 확장 프로그램입니다.

### Chrome 확장 프로그램 설치

1. **Chrome 웹 스토어 접속**
   - https://chromewebstore.google.com 접속

2. **Clawdbot 검색**
   - 검색창에 "Clawdbot" 입력
   - 또는 직접 링크: https://chromewebstore.google.com/detail/clawdbot-browser-relay/dgpmpijclocjgjbbejikaoofopnphaga

3. **확장 프로그램 추가**
   - **"Chrome에 추가"** 클릭
   - **"확장 프로그램 추가"** 확인

4. **확장 프로그램 고정**
   - 주소창 옆 퍼즐 아이콘 클릭
   - Clawdbot 옆 핀 아이콘 클릭

---

## 9. 테스트하기

### Clawdbot 시작

```bash
# 게이트웨이 시작
clawdbot gateway start

# 상태 확인
clawdbot status
```

### 웹 채팅으로 테스트

```bash
clawdbot chat
```

브라우저가 열리고 채팅창이 나타납니다. 여기서 대화해보세요!

### 텔레그램/슬랙으로 테스트

핸드폰에서 텔레그램 또는 슬랙 앱을 열고 봇에게 메시지를 보내보세요:

- "안녕!"
- "오늘 날씨 어때?"
- "간단한 HTML 페이지 만들어줘"

---

## 10. 문제 해결

### ❌ "API key is invalid" 오류

- Anthropic Console에서 API 키 다시 확인
- 결제 수단이 등록되어 있는지 확인
- 키를 복사할 때 앞뒤 공백이 없는지 확인

### ❌ 텔레그램 봇이 응답하지 않음

1. 봇 토큰이 정확한지 확인
2. allowlist에 내 Chat ID가 있는지 확인
3. `clawdbot gateway restart` 실행
4. `clawdbot gateway logs` 로 에러 확인

### ❌ 슬랙 봇이 응답하지 않음

1. Socket Mode가 활성화되어 있는지 확인
2. Event Subscriptions가 켜져 있는지 확인
3. Bot Token과 App Token이 정확한지 확인
4. allowlist에 내 User ID가 있는지 확인

### ❌ "Address already in use" 오류

포트가 이미 사용 중입니다:

```bash
# Windows
netstat -ano | findstr :18789
taskkill /PID <PID번호> /F

# macOS
lsof -ti:18789 | xargs kill -9
```

### ❌ Node.js 명령어가 안 됨

- 터미널/PowerShell을 껐다가 다시 열기
- 또는 컴퓨터 재부팅

---

## 🎉 완료!

이제 핸드폰에서 텔레그램이나 슬랙으로 메시지를 보내면, PC에서 Clawdbot이 작업을 수행합니다!

### 활용 예시

- "랜딩 페이지 만들어줘"
- "Python으로 계산기 프로그램 만들어줘"
- "내 화면 캡처해서 보여줘"
- "구글에서 OOO 검색해줘"

---

## 📚 추가 자료

- **공식 문서**: https://docs.clawd.bot
- **GitHub**: https://github.com/clawdbot/clawdbot
- **Discord 커뮤니티**: https://discord.com/invite/clawd

---

*Made with ❤️ by BSD 바이브코딩*
