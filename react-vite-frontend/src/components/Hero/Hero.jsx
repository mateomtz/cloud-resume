import React from 'react'
import heroImage from "../../assets/hero/heroImage.png";
import styles from "./Hero.module.css"

export const Hero = () => {
  return (
    <section className={styles.container}>
        <div className={styles.content}>
            <h1 className={styles.title}>Hi, I'm Mateo.</h1>
            <p className={styles.description}>I'm an IT Support professional with 3 years of experience supporting SaaS products and macOS and Windows systems.
                Reach out on my LinkedIn if you'd like to learn more.
            </p>
        </div>
        <img src={heroImage} alt="hero image of me" className={styles.heroImg}/>
            <div className={styles.topBlur}></div>
            <div className={styles.bottomBlur}></div>
    </section>
  )
    
}
