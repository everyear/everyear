import React, { useState } from 'react';
import Button from '@mui/material/Button';
import CssBaseline from '@mui/material/CssBaseline';
import TextField from '@mui/material/TextField';
import Autocomplete from '@mui/material/Autocomplete';
import Link from '@mui/material/Link';
import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select from '@mui/material/Select';
import InputLabel from '@mui/material/InputLabel';
import Checkbox from '@mui/material/Checkbox';
// import LockOutlinedIcon from '@mui/icons-material/LockOutlined';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import CheckboxesTags from '../components/CheckboxesTags';
// import { Select } from '@mui/material';

function Copyright(props) {
  return (
    <Typography variant="body2" color="text.secondary" align="center" {...props}>
      {'Copyright © '}
      <Link color="inherit" href="/home">
        EVERYEAR
      </Link>{' '}
      {new Date().getFullYear()}
      {'.'}
    </Typography>
  );
}

// const theme = createTheme();
const theme = createTheme({
  palette: {
    neutral: {
      main: '#E86F00',
      contrastText: '#fff',
    },
  },
});

export default function Register() {
  const yeardream_generations = [1, 2];
  
  // 필수 입력 정보 -> 성별 추가도 필요하지 않을지?
  const [Name, setName] = useState("");
  const [Sex, setSex] = useState("");
  const [Nickname, setNickname] = useState("");
  const [Email, setEmail] = useState("");
  const [Password, setPassword] = useState("");
  const [ConfirmPassword, setConfirmPassword] = useState("");
  const [Generation, setGeneration] = useState("");
  // 선택 입력 정보
  const [Birth, setBirth] = useState("");
  const [Interesting, setInteresting] = useState(new Set());
  const [Github, setGithub] = useState("");
  const [Blog, setBlog] = useState("");
  const [Intro, setIntro] = useState("");

  const onNameHandler = (event) => {
    setName(event.currentTarget.value);
  }
  const onSexHandler = (event) => {
    setSex(event.target.value);
  }
  const onNicknameHandler = (event) => {
    setNickname(event.currentTarget.value);
  }
  const onEmailHandler = (event) => {
    setEmail(event.currentTarget.value);
  }
  const onPasswordHandler = (event) => {
    setPassword(event.currentTarget.value);
  }
  const onConfirmPasswordHandler = (event) => {
    setConfirmPassword(event.currentTarget.value);
  }
  const onGenerationHandler = (event) => {
    setGeneration(event.target.value);
  }
  const onBirthHandler = (event) => {
    setBirth(event.currentTarget.value);
  }
  // const onInterestingHandler = (event) => {
  //   console.log(event);
  //   setInteresting([event.currentTarget.value]);
  // }
  const onGithubHandler = (event) => {
    setGithub(event.currentTarget.value);
  }
  const onBlogHandler = (event) => {
    setBlog(event.currentTarget.value);
  }
  const onIntroHandler = (event) => {
    setIntro(event.currentTarget.value);
  }

  const hasError = passwordEntered => (Password.length < 5 && Password.length > 0) ? true : false;
  const hasNotSameError = passwordEntered => (Password != ConfirmPassword) ? true : false;

  const handleSubmit = (event) => {
    event.preventDefault();
    const data = new FormData(event.currentTarget);
    console.log(data.get('interestings'));
    console.log({
      // email: data.get('email'),
      // password: data.get('password'),
      "Name": Name,
      "Sex": Sex,
      "Nick": Nickname,
      "Email": Email,
      "Password": Password,
      "Gen": Generation,
      "Birth": Birth,
      "Inter": Interesting,
      "Git": Github,
      "Blog": Blog,
      "Intro": Intro,
    });
    const i = [...Interesting];
    i.sort();
    console.log(i);
  };

  return (
    <ThemeProvider theme={theme}>
      <Container component="main" maxWidth="xs">
        <CssBaseline />
        <Box
          sx={{
            marginTop: 8,
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
          }}
        >
          {/* <Avatar sx={{ m: 1, bgcolor: 'secondary.main' }}>
            <LockOutlinedIcon />
          </Avatar> */}
          <Typography component="h1" variant="h5">
            EVERYEAR 회원가입
          </Typography>
          <Box component="form" noValidate onSubmit={handleSubmit} sx={{ mt: 3 }}>
            <Grid container spacing={2}>
              <Grid item xs={12} mt={2}>
                필수 입력 정보
              </Grid>
              <Grid item xs={12}>
                <TextField 
                  required
                  color="neutral"
                  fullWidth
                  value={Name}
                  onChange={onNameHandler}
                  id="name"
                  name="name"
                  label="이름"
                  autoFocus
                />
              </Grid>
              <Grid item xs={12}>
                <FormControl fullWidth>
                  <InputLabel required id="sex-label" color="neutral">성별</InputLabel>
                  <Select
                    required
                    id="sex"
                    name="sex"
                    value={Sex}
                    label="성별"
                    onChange={onSexHandler}
                    color="neutral"
                    >
                    <MenuItem value="male">남자</MenuItem>
                    <MenuItem value="female">여자</MenuItem>
                    {/* <MenuItem value="">선택 안 함</MenuItem> */}
                  </Select>
                </FormControl>
              </Grid>
              <Grid item xs={12}>
                <TextField
                  required
                  color="neutral"
                  fullWidth
                  value={Nickname}
                  onChange={onNicknameHandler}
                  label="닉네임"
                  type="text"
                  id="nickname"
                  name="nickname"
                  autoComplete="nickname"
                />
              </Grid>
              <Grid item xs={12}>
                <TextField
                  required
                  color="neutral"
                  fullWidth
                  value={Email}
                  onChange={onEmailHandler}
                  id="email"
                  name="email"
                  label="이메일"
                  autoComplete="email"
                />
              </Grid>
              <Grid item xs={12}>
                <TextField
                  required
                  color="neutral"
                  fullWidth
                  value={Password}
                  onChange={onPasswordHandler}
                  error={hasError("password")}
                  helperText={
                    hasError('confirmPassword') ? "안전을 위해 5글자 이상의 비밀번호로 설정해주세요." : null
                  }
                  label="비밀번호(5글자 이상)"
                  type="password"
                  id="password"
                  name="password"
                  autoComplete="new-password"
                />
              </Grid>
              <Grid item xs={12}>
                <TextField
                  required
                  color="neutral"
                  fullWidth
                  value={ConfirmPassword}
                  onChange={onConfirmPasswordHandler}
                  error={hasNotSameError('confirmPassword')} // 해당 텍스트필드에 error 핸들러 추가
                  helperText={
                    hasNotSameError('confirmPassword') ? "입력한 비밀번호와 일치하지 않습니다." : null
                  }
                  label="비밀번호 재확인"
                  type="password"
                  id="confirmPassword"
                  name="confirmPassword"
                  autoComplete="new-password"
                />
              </Grid>
              <Grid item xs={12}>
                <FormControl fullWidth>
                  <InputLabel required id="generation-label" color="neutral">이어드림 기수</InputLabel>
                  <Select
                    required
                    id="generation"
                    name="generation"
                    value={Generation}
                    label="이어드림 기수"
                    onChange={onGenerationHandler}
                    color="neutral"
                    >
                    <MenuItem value="1">1기</MenuItem>
                    <MenuItem value="2">2기</MenuItem>
                  </Select>
                </FormControl>
              </Grid>
              <Grid item xs={12} mt={2}>
                선택 입력 정보
              </Grid>
              <Grid item xs={12}>
                <TextField
                  fullWidth
                  color="neutral"
                  value={Birth}
                  onChange={onBirthHandler}
                  label="생년월일"
                  helperText="YYMMDD 형식(주민등록번호 앞 6자리)으로 입력"
                  type="text"
                  id="birth"
                  name="birth"
                  autoComplete="birth"
                />
              </Grid>
              <Grid item xs={12}>
                <CheckboxesTags myValue={Interesting} myFunc={setInteresting} color="neutral" />
              </Grid>
              <Grid item xs={12}>
                <TextField
                  fullWidth
                  color="neutral"
                  value={Github}
                  onChange={onGithubHandler}
                  label="Github URL"
                  type="text"
                  id="github-url"
                  name="github"
                  autoComplete="github-url"
                />
              </Grid>
              <Grid item xs={12}>
                <TextField
                  fullWidth
                  color="neutral"
                  value={Blog}
                  onChange={onBlogHandler}
                  label="개인 블로그 URL"
                  type="text"
                  id="blog"
                  name="blog"
                  autoComplete="blog"
                />
              </Grid>
              <Grid item xs={12}>
                <TextField
                  fullWidth
                  color="neutral"
                  value={Intro}
                  onChange={onIntroHandler}
                  label="간략한 자기 소개"
                  type="text"
                  id="intro"
                  name="intro"
                  autoComplete="intro"
                  multiline
                  rows={5}
                />
              </Grid>
              {/* <Grid item xs={12}>
                <FormControlLabel
                  control={<Checkbox value="allowExtraEmails" color="primary" />}
                  label="I want to receive inspiration, marketing promotions and updates via email."
                />
              </Grid> */}
            </Grid>
            <Button
              // href="/"
              type="submit"
              fullWidth
              color="neutral"
              variant="contained"
              sx={{ mt: 3, mb: 2 }}
            >
              가입하기
            </Button>
            <Grid container justifyContent="flex-end">
              <Grid item>
                <Link href="/login" variant="body2" color="inherit">
                  이미 계정이 있으신가요?
                </Link>
              </Grid>
            </Grid>
          </Box>
        </Box>
        <Copyright sx={{ mt: 5, mb: 10 }} />
      </Container>
    </ThemeProvider>
  );
}