import * as React from 'react';
import CssBaseline from '@mui/material/CssBaseline';
import Grid from '@mui/material/Grid';
import Container from '@mui/material/Container';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import Header from './Header';
import MainFeaturedPost from './MainFeaturedPost';
import FeaturedPost from './FeaturedPost';
import Footer from './Footer';

const sections = [
  { title: '자유게시판', url: '#' },
  { title: '정보게시판', url: '#' },
  { title: '질문게시판', url: '#' },
];

const mainFeaturedPost = {
  title: '에브리 이어',
  description_1:
  '"스타트업 청년인재 이어드림 프로젝트"의',
  description_2:
  '예비 및 현역 수강생, 그리고 수료생을 위한',
  description_3:
  '정보 공유 및 커뮤니티 사이트',
  image: './home_cover.jpg',
  imageText: 'main image description',
  linkText: '',
};

const featuredPosts = [
  {
    title: '자유게시판 핫글',
    date: 'mm/dd',
    description:
      '자유게시판의 핫글 내용 일부',
    image: '',
    imageLabel: '', 
  },
  {
    title: '정보게시판 핫글',
    date: 'mm/dd',
    description:
      '정보게시판의 핫글 내용 일부',
    image: '',
    imageLabel: '', 
  },
  {
    title: '질문게시판 핫글',
    date: 'mm/dd',
    description:
      '질문게시판의 핫글 내용 일부',
    image: '',
    imageLabel: '', 
  },
];

// const posts = [post1, post2, post3];
const theme = createTheme();

export default function Blog() {
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Container maxWidth="lg">
        <Header title="EVERYEAR" sections={sections} />
        <main>
          <MainFeaturedPost post={mainFeaturedPost} />
          <Grid container spacing={4}>
            {featuredPosts.map((post) => (
              <FeaturedPost key={post.title} post={post} />
            ))}
          </Grid>
          {/* <Grid container spacing={5} sx={{ mt: 3 }}>
            <Main title="From the firehose" posts={posts} />
          </Grid> */}
        </main>
      </Container>
      <Footer
        title=""
        description="Something here to give the footer a purpose!"
      />
    </ThemeProvider>
  );
}