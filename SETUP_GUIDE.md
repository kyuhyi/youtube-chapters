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

## 6. 텔레그램 연동 (상세 가이드)

> ⏱️ 예상 소요시간: 5분

텔레그램은 설정이 가장 간단합니다. 봇 토큰과 내 Chat ID만 있으면 됩니다.

---

### 📱 STEP 1: 텔레그램 앱 준비

**핸드폰 또는 PC에서 텔레그램 앱을 엽니다.**

- 텔레그램이 없다면: https://telegram.org 에서 다운로드
- 계정이 없다면: 전화번호로 회원가입

---

### 🤖 STEP 2: BotFather에서 봇 생성하기

BotFather는 텔레그램의 공식 봇 생성 도구입니다.

#### 2-1. BotFather 찾기

1. 텔레그램 상단의 **검색창** (돋보기 아이콘) 클릭
2. `@BotFather` 입력
3. 검색 결과에서 **파란색 체크마크 ✓** 가 있는 계정 선택
   - ⚠️ 가짜 계정 주의! 반드시 파란 체크 확인!

#### 2-2. BotFather와 대화 시작

1. BotFather 채팅방에 들어가면 **"시작"** 또는 **"Start"** 버튼 클릭
2. BotFather가 명령어 목록을 보여줍니다

#### 2-3. 새 봇 생성

1. 채팅창에 아래 명령어 입력 후 전송:
   ```
   /newbot
   ```

2. BotFather가 물어봅니다: **"Alright, a new bot. How are we going to call it? Please choose a name for your bot."**
   
   → 봇의 **표시 이름** 입력 (한글 가능)
   ```
   나의 AI 비서
   ```

3. BotFather가 다시 물어봅니다: **"Good. Now let's choose a username for your bot..."**
   
   → 봇의 **고유 아이디** 입력
   ```
   my_clawdbot_12345_bot
   ```
   
   ⚠️ **중요한 규칙:**
   - 반드시 `bot` 또는 `_bot`으로 끝나야 함
   - 영문, 숫자, 밑줄(_)만 사용 가능
   - 이미 존재하는 이름이면 다른 이름 사용

#### 2-4. 봇 토큰 저장 ⭐ (매우 중요!)

봇 생성이 완료되면 BotFather가 이런 메시지를 보냅니다:

```
Done! Congratulations on your new bot. You will find it at t.me/my_clawdbot_12345_bot.

Use this token to access the HTTP API:
7123456789:AAHxxx_YOUR_BOT_TOKEN_HERE_xxxxx

Keep your token secure and store it safely...
```

**`7123456789:AAHxxx...` 형태의 토큰을 복사해서 메모장에 저장하세요!**

이 토큰은 다시 볼 수 없으니 반드시 저장!

---

### 🔍 STEP 3: 내 Chat ID 확인하기

Clawdbot이 나에게만 응답하도록 하려면 내 Chat ID가 필요합니다.

#### 3-1. userinfobot 찾기

1. 텔레그램 검색창에서 `@userinfobot` 검색
2. **"User Info Bot"** 선택 (로봇 아이콘)

#### 3-2. Chat ID 확인

1. userinfobot 채팅방에서 **"시작"** 클릭
2. 아무 메시지나 보내기 (예: "안녕")
3. 봇이 내 정보를 보여줍니다:

```
@사용자이름
Id: 123456789      ← 이 숫자가 내 Chat ID!
First: 이름
Lang: ko
```

**`Id:` 뒤의 숫자를 복사해서 메모장에 저장하세요!**

---

### ⚙️ STEP 4: Clawdbot 설정 파일 수정

이제 Clawdbot에 텔레그램 정보를 입력합니다.

#### 4-1. 설정 파일 열기

터미널(또는 PowerShell)에서 아래 명령어 실행:

```bash
clawdbot config edit
```

설정 파일이 텍스트 에디터에서 열립니다.

#### 4-2. 텔레그램 설정 추가

파일 맨 아래에 다음 내용을 추가하세요:

```yaml
channels:
  telegram:
    enabled: true
    token: "여기에_BotFather에서_받은_토큰_붙여넣기"
    allowlist:
      - "여기에_내_ChatID_숫자_붙여넣기"
```

**실제 예시:**
```yaml
channels:
  telegram:
    enabled: true
    token: "7123456789:AAHxxx_YOUR_BOT_TOKEN_HERE_xxxxx"
    allowlist:
      - "123456789"
```

⚠️ **주의사항:**
- 토큰은 반드시 **큰따옴표(" ")** 로 감싸기
- Chat ID도 **큰따옴표(" ")** 로 감싸기 (숫자지만 문자열로 입력)
- `allowlist:` 아래 `-` 앞에 **스페이스 2칸** 들여쓰기

#### 4-3. 파일 저장 후 닫기

- Windows: `Ctrl + S` → 창 닫기
- macOS: `Cmd + S` → 창 닫기

---

### 🔄 STEP 5: Clawdbot 재시작

설정을 적용하려면 Clawdbot을 재시작해야 합니다.

```bash
clawdbot gateway restart
```

정상적으로 시작되면 이런 메시지가 나옵니다:
```
✓ Gateway restarted
```

**에러가 나면?**
```bash
# 로그 확인
clawdbot gateway logs
```

---

### ✅ STEP 6: 연결 테스트

#### 6-1. 내 봇 찾기

1. 텔레그램 검색창에서 아까 만든 봇 이름 검색
   - 예: `@my_clawdbot_12345_bot`
2. 봇 채팅방 들어가기

#### 6-2. 대화 시작

1. **"시작"** 또는 **"/start"** 클릭/입력
2. 아무 메시지나 보내보기:
   ```
   안녕! 넌 누구야?
   ```

#### 6-3. 응답 확인

몇 초 후 Clawdbot이 응답하면 **성공!** 🎉

**응답이 없다면?**
- 터미널에서 `clawdbot status` 실행해서 상태 확인
- `clawdbot gateway logs` 로 에러 확인
- 토큰과 Chat ID가 정확한지 다시 확인

---

### 🎯 텔레그램 연동 체크리스트

- [ ] BotFather에서 봇 생성 완료
- [ ] 봇 토큰 저장함 (`7xxxxxxxxxx:AAHxxxxx...`)
- [ ] userinfobot에서 내 Chat ID 확인함
- [ ] `clawdbot config edit`으로 설정 추가함
- [ ] `clawdbot gateway restart` 실행함
- [ ] 봇과 대화 테스트 성공!

---
---

## 7. 슬랙 연동 (상세 가이드)

> ⏱️ 예상 소요시간: 10-15분

슬랙은 텔레그램보다 설정이 복잡하지만, 단계별로 따라하면 됩니다.

**필요한 것:**
- Slack 워크스페이스 (무료/유료 모두 가능)
- 워크스페이스 관리자 권한 또는 앱 설치 권한

---

### 🌐 STEP 1: Slack API 사이트 접속

1. 웹 브라우저에서 아래 주소 접속:
   ```
   https://api.slack.com/apps
   ```

2. 우측 상단 **"Sign in"** 클릭

3. Slack 계정으로 로그인
   - 워크스페이스 선택 화면이 나오면, Clawdbot을 연결할 워크스페이스 선택

---

### 📦 STEP 2: 새 Slack App 만들기

#### 2-1. Create New App 클릭

1. 로그인 후 보이는 화면에서 **"Create New App"** 버튼 클릭
   - 버튼이 안 보이면: 우측 상단 **"Your Apps"** → **"Create New App"**

#### 2-2. 생성 방식 선택

팝업이 뜨면 **"From scratch"** 선택
- ❌ "From an app manifest" 아님!

#### 2-3. 앱 정보 입력

1. **App Name**: `Clawdbot` (원하는 이름 입력)
2. **Pick a workspace**: Clawdbot을 사용할 워크스페이스 선택
3. **"Create App"** 버튼 클릭

---

### 🔑 STEP 3: Bot Token 권한 설정

봇이 메시지를 읽고 보낼 수 있도록 권한을 부여합니다.

#### 3-1. OAuth & Permissions 메뉴로 이동

1. 좌측 사이드바에서 **"OAuth & Permissions"** 클릭
   - Features 섹션 아래에 있음

#### 3-2. Bot Token Scopes 찾기

1. 페이지를 아래로 스크롤
2. **"Scopes"** 섹션 찾기
3. **"Bot Token Scopes"** 영역 확인
   - ⚠️ "User Token Scopes" 아님! **Bot Token Scopes** 맞는지 확인!

#### 3-3. 권한(Scopes) 추가하기

**"Add an OAuth Scope"** 버튼을 클릭해서 아래 권한들을 **하나씩** 추가:

| 권한 이름 | 설명 |
|-----------|------|
| `app_mentions:read` | @멘션 읽기 |
| `channels:history` | 공개 채널 메시지 읽기 |
| `channels:read` | 공개 채널 목록 보기 |
| `chat:write` | 메시지 보내기 |
| `groups:history` | 비공개 채널 메시지 읽기 |
| `groups:read` | 비공개 채널 목록 보기 |
| `im:history` | DM 메시지 읽기 |
| `im:read` | DM 목록 보기 |
| `im:write` | DM 보내기 |
| `users:read` | 사용자 정보 읽기 |

**추가 방법:**
1. "Add an OAuth Scope" 클릭
2. 검색창에 권한 이름 입력 (예: `app_mentions:read`)
3. 목록에서 해당 권한 클릭
4. 10개 모두 반복!

#### 3-4. 워크스페이스에 앱 설치

권한을 다 추가했으면:

1. 페이지 맨 위로 스크롤
2. **"OAuth Tokens for Your Workspace"** 섹션 찾기
3. **"Install to Workspace"** 버튼 클릭
4. 권한 요청 화면에서 **"허용"** 클릭

#### 3-5. Bot User OAuth Token 복사 ⭐

설치가 완료되면 **"Bot User OAuth Token"** 이 생성됩니다.

```
xoxb-여러숫자-여러숫자-영문자조합
```

**이 토큰을 복사해서 메모장에 저장하세요!**

- 토큰은 `xoxb-`로 시작함
- 페이지를 벗어나도 다시 볼 수 있지만, 지금 복사해두는 게 편함

---

### 🔐 STEP 4: App-Level Token 생성

Socket Mode 연결에 필요한 토큰입니다.

#### 4-1. Basic Information 메뉴로 이동

1. 좌측 사이드바에서 **"Basic Information"** 클릭
   - Settings 섹션 아래에 있음

#### 4-2. App-Level Tokens 섹션 찾기

1. 페이지를 아래로 스크롤
2. **"App-Level Tokens"** 섹션 찾기

#### 4-3. 새 토큰 생성

1. **"Generate Token and Scopes"** 버튼 클릭
2. 팝업이 뜨면:
   - **Token Name**: `socket` (아무 이름이나 OK)
   - **"Add Scope"** 클릭 → `connections:write` 선택
3. **"Generate"** 버튼 클릭

#### 4-4. App-Level Token 복사 ⭐

생성된 토큰이 표시됩니다:

```
xapp-숫자-영문자조합-영문숫자조합...
```

**이 토큰을 복사해서 메모장에 저장하세요!**

- 토큰은 `xapp-`으로 시작함
- **"Done"** 클릭하면 팝업이 닫힘
- 나중에 다시 보려면 토큰 옆 **"..."** 클릭 → **"Copy"**

---

### ⚡ STEP 5: Socket Mode 활성화

Slack과 실시간 통신을 위해 Socket Mode를 켭니다.

#### 5-1. Socket Mode 메뉴로 이동

1. 좌측 사이드바에서 **"Socket Mode"** 클릭
   - Settings 섹션 아래에 있음

#### 5-2. Socket Mode 켜기

1. **"Enable Socket Mode"** 토글을 **ON** 으로 변경
2. 이미 App-Level Token이 있으면 자동 연결됨

---

### 📨 STEP 6: Event Subscriptions 설정

Clawdbot이 메시지를 수신하려면 이벤트 구독이 필요합니다.

#### 6-1. Event Subscriptions 메뉴로 이동

1. 좌측 사이드바에서 **"Event Subscriptions"** 클릭
   - Features 섹션 아래에 있음

#### 6-2. 이벤트 구독 켜기

1. **"Enable Events"** 토글을 **ON** 으로 변경

#### 6-3. Bot Events 추가

1. 페이지 아래로 스크롤
2. **"Subscribe to bot events"** 섹션 찾기
3. 접혀 있으면 클릭해서 펼치기
4. **"Add Bot User Event"** 버튼 클릭

아래 이벤트들을 **하나씩** 추가:

| 이벤트 이름 | 설명 |
|-------------|------|
| `app_mention` | @멘션 받았을 때 |
| `message.channels` | 공개 채널 메시지 |
| `message.groups` | 비공개 채널 메시지 |
| `message.im` | DM 메시지 |

#### 6-4. 변경사항 저장

1. 페이지 하단의 **"Save Changes"** 버튼 클릭
2. 초록색 "Success" 메시지 확인

---

### 👤 STEP 7: 내 Slack User ID 확인

Clawdbot이 나에게만 응답하도록 설정하려면 내 User ID가 필요합니다.

#### 7-1. Slack 앱에서 내 프로필 열기

**방법 A - 데스크톱 앱/웹:**
1. 좌측 상단 워크스페이스 이름 클릭
2. **"프로필"** 클릭 (또는 내 이름 클릭)

**방법 B - 모바일 앱:**
1. 하단 탭에서 **"나"** 선택

#### 7-2. 멤버 ID 복사

1. 프로필 화면에서 **더보기(⋯)** 클릭
2. **"멤버 ID 복사"** 클릭

ID 형태: `U01ABCD2EFG` (영문+숫자 11자리)

**이 ID를 메모장에 저장하세요!**

---

### ⚙️ STEP 8: Clawdbot 설정 파일 수정

이제 Clawdbot에 슬랙 정보를 입력합니다.

#### 8-1. 설정 파일 열기

터미널(또는 PowerShell)에서:

```bash
clawdbot config edit
```

#### 8-2. 슬랙 설정 추가

파일에 다음 내용을 추가하세요:

**텔레그램 설정이 이미 있는 경우:**
```yaml
channels:
  telegram:
    enabled: true
    token: "텔레그램토큰"
    allowlist:
      - "텔레그램ChatID"
  slack:
    enabled: true
    botToken: "여기에_Bot_User_OAuth_Token_붙여넣기"
    appToken: "여기에_App_Level_Token_붙여넣기"
    allowlist:
      - "여기에_내_User_ID_붙여넣기"
```

**슬랙만 사용하는 경우:**
```yaml
channels:
  slack:
    enabled: true
    botToken: "여기에_Bot_User_OAuth_Token_붙여넣기"
    appToken: "여기에_App_Level_Token_붙여넣기"
    allowlist:
      - "여기에_내_User_ID_붙여넣기"
```

**실제 예시:**
```yaml
channels:
  slack:
    enabled: true
    botToken: "여기에-복사한-Bot-User-OAuth-Token"
    appToken: "여기에-복사한-App-Level-Token"
    allowlist:
      - "U01ABCD2EFG"
```

⚠️ **주의사항:**
- 모든 값은 **큰따옴표(" ")** 로 감싸기
- `channels:` 아래 들여쓰기 **스페이스 2칸**
- `slack:` 아래 들여쓰기 **스페이스 4칸**
- 토큰 앞뒤에 공백이 들어가지 않도록 주의!

#### 8-3. 파일 저장 후 닫기

- Windows: `Ctrl + S` → 창 닫기
- macOS: `Cmd + S` → 창 닫기

---

### 🔄 STEP 9: Clawdbot 재시작

```bash
clawdbot gateway restart
```

성공 메시지:
```
✓ Gateway restarted
```

**에러 확인:**
```bash
clawdbot gateway logs
```

자주 나오는 에러:
- `invalid_auth` → Bot Token이 잘못됨
- `connection_error` → App Token이 잘못되거나 Socket Mode가 꺼져있음

---

### ✅ STEP 10: 연결 테스트

#### 10-1. Slack에서 Clawdbot 앱 찾기

1. Slack 앱 열기
2. 좌측 사이드바 맨 아래 **"앱"** 섹션 찾기
3. **"앱 추가"** 또는 **"+"** 클릭
4. `Clawdbot` 검색
5. 클릭해서 DM 채팅방 열기

#### 10-2. 메시지 보내기

DM 채팅방에서:
```
안녕! 넌 누구야?
```

#### 10-3. 응답 확인

몇 초 후 Clawdbot이 응답하면 **성공!** 🎉

**채널에서 사용하려면:**
1. 원하는 채널로 이동
2. 채널 설정 → **"통합"** → **"앱 추가"** → Clawdbot 추가
3. `@Clawdbot 안녕!` 처럼 멘션해서 사용

---

### 🎯 슬랙 연동 체크리스트

- [ ] Slack API 사이트에서 새 앱 생성
- [ ] OAuth & Permissions에서 Bot Token Scopes 10개 추가
- [ ] 워크스페이스에 앱 설치 완료
- [ ] Bot User OAuth Token 저장함 (`xoxb-...`)
- [ ] Basic Information에서 App-Level Token 생성
- [ ] App-Level Token 저장함 (`xapp-...`)
- [ ] Socket Mode 활성화함 (ON)
- [ ] Event Subscriptions 활성화함 (ON)
- [ ] Bot Events 4개 추가함
- [ ] Save Changes 클릭함
- [ ] 내 Slack User ID 확인함 (`U0...`)
- [ ] `clawdbot config edit`으로 설정 추가함
- [ ] `clawdbot gateway restart` 실행함
- [ ] 봇과 DM 테스트 성공!

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
