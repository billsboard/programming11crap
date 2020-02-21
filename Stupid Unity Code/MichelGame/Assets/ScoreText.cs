using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class ScoreText : MonoBehaviour
{

    int score = 0;

    Text text;

    // Start is called before the first frame update
    void Start()
    {
        text = GetComponent<Text>();
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    public void changeScore(int scoreIncrement) {
        text.text = "Score: " + (score + scoreIncrement).ToString();
        score += scoreIncrement;
    }
}
