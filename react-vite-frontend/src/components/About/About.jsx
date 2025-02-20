import React from 'react'
import styles from "./About.module.css"
import aboutImage from "../../assets/about/aboutImage.png";
import cursorIcon from "../../assets/about/cursorIcon.png";
import serverIcon from "../../assets/about/serverIcon.png";
import uiIcon from "../../assets/about/uiIcon.png";


export const About = () => {
  return (
    <section className={styles.container}>
        <h2 className={styles.title}>About</h2>
        <div className={styles.content}>
            <img 
            src={aboutImage} 
            alt='me sitting with a laptop'
            className={styles.aboutImage}
            />
            <ul className={styles.aboutItems}>
                <li className={styles.aboutItem}>
                    <img src={cursorIcon}/>
                    <div className={styles.aboutItemText}>
                        <h3>IT Support Analyst</h3>
                        <p>I'm an IT Support Analst with experienc in support macOS and Windows environments.</p>
                    </div>
                </li>
                <li className={styles.aboutItem}>
                    <img 
                    src={serverIcon}
                    alt="server icon"
                    />
                    <div className={styles.aboutItemText}>
                        <h3>Placeholder</h3>
                        <p>Add text concerning another area where I have experience</p>
                    </div>
                </li>
                <li className={styles.aboutItem}>
                    <img 
                    src={uiIcon}
                    alt="ui icon"
                    />
                    <div className={styles.aboutItemText}>
                        <h3>Another Placeholder</h3>
                        <p>Add text concerning another area where I have experience</p>
                    </div>
                </li>
            </ul>
        </div>
    </section>
  )
}
