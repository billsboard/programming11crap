using System.Collections;
using System.Collections.Generic;
using TMPro;
using UnityEngine;

public class GameStart : MonoBehaviour
{

    public int targetCount;
    public int maxPositiveScore;
    public int minPositiveScore;
    public int maxNegativeScore;
    public int minNegativeScore;
    public float negativePercentage;

    public GameObject target;

    

    // Start is called before the first frame update
    void Start()
    {
        /*
        for (int i = 0; i < targetCount; i++)
        {
            int x = Random.Range(1, 100);
            int score;

            if (x <= negativePercentage)
            {
                score = Random.Range(maxNegativeScore, minNegativeScore);
            }
            else
            {
                score = Random.Range(minPositiveScore, maxPositiveScore);
            }

            GameObject hitTarget = Instantiate(target, new Vector3(Random.Range(-3, 3) * 3, Random.Range(-1, 1) * 4, 0), new Quaternion(0, 0, 0, 0));
        }*/
    }

    // Update is called once per frame
    void Update()
    {

    }
}
