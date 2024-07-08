import Movie from "../../components/movie"
import styles from "../../styles/home.module.css"
import { API_URL } from "../constants"


export const metadata = {
  title : "home",
}



async function getMovies(){
  await new Promise((resolve) => setTimeout(resolve, 1000))
  const response = await fetch(API_URL)
  const json = await response.json()
  return json
}

// function 이름은 별로 상관 없음
export default async function Page() {
  const movies = await getMovies() 
  
  return (
    <div className={styles.container}>
      {movies.map(movie => 
        <Movie 
          key={movie.id} 
          id={movie.id} 
          poster_path={movie.poster_path} 
          title={movie.title} 
        />
      )}
    </div>
  )
}