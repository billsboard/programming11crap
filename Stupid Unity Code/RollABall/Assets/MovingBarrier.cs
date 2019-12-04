using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MovingBarrier : MonoBehaviour
{
    // Start is called before the first frame update

    // Update is called once per frame
    public int level;

    public int posLimit = 25;
    public int negLimit = 25;


    public float speed = 15;

    public bool startOpposite = false;

    Vector3 velocity;




    private void Start()
    {
        posLimit -= (int)(GetComponent<Collider>().bounds.size.z / 2);
        negLimit -= (int)(GetComponent<Collider>().bounds.size.z / 2);

        if (!startOpposite)
        {
            velocity = new Vector3(0, 0, speed);
        }
        else
        {
            velocity = new Vector3(0, 0, -speed);

        }


    }

    private void Update()
    {

        if (OnCollision.currentLevel == level)
        {
            if (transform.localPosition.z <= 13 - negLimit)
            {
                velocity = new Vector3(0, 0, Math.Abs(speed));
            }
            else if (transform.localPosition.z >= 13 + posLimit)
            {
                velocity = new Vector3(0, 0, Math.Abs(speed)*-1);
            }

            transform.position += velocity * Time.deltaTime;

        }

    }
}
