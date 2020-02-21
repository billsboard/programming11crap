using System.Collections;
using System.Collections.Generic;
using TMPro;
using UnityEngine;

public class TargetSpawn : MonoBehaviour
{

    public int maxScore;
    public int minScore;

    public int convertToPositiveThreshold = -3;
    public float swapTimer = 3.0f;

    public bool freeze = false;

    private int score;
    private float timer;

    private bool clicked;
    private GameObject scoreColor;
    // Start is called before the first frame update
    void Start()
    {
        scoreColor = transform.Find("TargetHit").gameObject;
        setRandomScore();
    }

    // Update is called once per frame
    void Update()
    {

        if (freeze)
        {
            return;
        }
        timer += Time.deltaTime;

        if(timer >= swapTimer)
        {
            setRandomScore();
            timer = 0;
            clicked = false;
        }
    }

    void OnMouseDown()
    {
        if (clicked || freeze)
        {
            return;
        }

        clicked = true;
        GetComponentInChildren<TextMeshPro>().text = "";
        scoreColor.GetComponent<Renderer>().material.color = new Color(0.6235294f, 0.1254493f, 0.01568626f, 0);
        GameObject.Find("Score").GetComponent<ScoreText>().changeScore(score);
    }

    private void setRandomScore()
    {
        score = Random.Range(minScore, maxScore);
        if (score == 0)
        {
            score = 1;
        }
        else if (score >= convertToPositiveThreshold)
        {
            score = Mathf.Abs(score);
        }

        if(score > 0)
        {
            scoreColor.GetComponent<Renderer>().material.color = new Color(0.3153267f, 0.6226415f, 0.01468494f);
        }
        else
        {
            scoreColor.GetComponent<Renderer>().material.color = new Color(0.6235294f, 0.1254493f, 0.01568626f);
        }

        GetComponentInChildren<TextMeshPro>().text = score.ToString();
    }
}
