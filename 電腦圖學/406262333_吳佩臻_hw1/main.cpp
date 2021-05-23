/**
 * Example of Using OpenGL 2.x Drawing a rotating triangle
 */
#include <glad/glad.h>
#define GLFW_INCLUDE_NONE
#include <GLFW/glfw3.h>

//#include <GLUT/glut.h>

#include <cmath>
#include <stdlib.h>
#include <stdio.h>


using namespace std;


static void error_callback(int error, const char *description)
{
    fprintf(stderr, "Error: %s\n", description);
}

GLFWwindow *window;

void onInit()
{

    glfwSetErrorCallback(error_callback);

    if (!glfwInit())
        exit(EXIT_FAILURE);

    // Specify the OpenGL version
    glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 2);
    glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 0);

    // Construct Window
    window = glfwCreateWindow(900, 900, "HW1", NULL, NULL);
    if (!window)
    {
        glfwTerminate();
        exit(EXIT_FAILURE);
    }
    // Keyboard input
    // Load OpenGL
    glfwMakeContextCurrent(window);
    gladLoadGLLoader((GLADloadproc)glfwGetProcAddress); // https://stackoverflow.com/questions/58053885/having-an-issue-with-gladloadgl-im-getting-an-error-saying-it-does-not-take
    glfwSwapInterval(1);


}

// Resize with the viewport
float cameraZoom = 1.f;
void onResize()
{
    float ratio;
    int width, height;

    // Set viewport size
    glfwGetFramebufferSize(window, &width, &height);
    ratio = width / (float)height;
    glViewport(0, 0, width, height);

    // Setting up orthographic projection (for 2D)
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    glOrtho(-(cameraZoom*ratio), (cameraZoom*ratio), -cameraZoom, cameraZoom, -100, 100);
    //
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
}

float rotateDegree = 0.f;
void onUpdate()
{
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
}

void rectangle(double x1, double y1, double x_len, double y_len  ,int r , int g , int b)
{
    glColor3ub(r, g, b);
    glVertex2f(x1,y1) ;
    glVertex2f(x1,y1+y_len) ;
    glVertex2f(x1+x_len,y1+y_len) ;
    glVertex2f(x1+x_len,y1) ;

}
int col = 5;
int row = 7;
const int num = 35;
double RectX[num];
double RectY[num];
bool RectShow[num];
int heart = 3;
void CreateRectangle()
{
    // 方塊X座標
    double TempPositionX = -0.9f;
    double TempPositionY = 0.8f;
    for(int i=0 ; i<col*row ;i++)
    {
        RectX[i] = TempPositionX;
        TempPositionX += 0.3f;
        if(i % col == col-1 )
            TempPositionX = -0.9f;

        RectY[i] = TempPositionY;
        TempPositionY -= 0.125f;
        if(i % row == row-1 )
            TempPositionY =  0.8f;

        RectShow[i] = 1;
    }
}
double DX = 0.0,DY = -0.75;
double D2X = 0.8f,D2Y = 0.0f;
bool StartGame = false;
int Level =1;
int DistoryRectNumber = 0   ;
double speed = 0.025f;
int KeyBoardInput(GLFWwindow *window)
{
    if (glfwGetKey(window, GLFW_KEY_A) == GLFW_PRESS)
    {
        if(DX>=-1)
            DX -= speed;
    }
    else if (glfwGetKey(window, GLFW_KEY_D) == GLFW_PRESS)
    {
        if(DX <= 0.75)
         DX += speed;
    }
    else if(glfwGetKey(window, GLFW_KEY_SPACE) == GLFW_PRESS) // start game
    {
        if(StartGame == false && Level == 2)
        {
            DistoryRectNumber = 0; 
            StartGame = true;
        }
        else if(StartGame == false && Level == 1)
        {
            StartGame = true;
        }
    }
    else if(glfwGetKey(window, GLFW_KEY_S) == GLFW_PRESS)
    {
        if(D2Y>=-1)
            D2Y -= speed;
    }
    else if(glfwGetKey(window, GLFW_KEY_W) == GLFW_PRESS)
    {
         if(D2Y <= 0.75)
         D2Y += speed;
    }
}

double BX = 0;
int xPath = 1;
int yPath = 1;
double BY = 0;
void onRender()
{
    glClear(GL_COLOR_BUFFER_BIT);

    // Start Drawing here
    glBegin(GL_QUADS);
    {
        // 障礙物
        bool TempColor = 0;
        for(int i=0 ; i<col*row ; i++)
        {
            if(i % col == 0)
                TempColor = !TempColor;
            if(TempColor && RectShow[i])
                rectangle(RectX[i],RectY[i],0.25,0.075,119, 46, 37);
            else if(!TempColor &&  RectShow[i])
                rectangle(RectX[i],RectY[i],0.25,0.075,25, 114, 120);
        }
        // 下方移動桿
        rectangle(DX,DY,0.25,0.075,255, 424, 186);

        if(Level == 2)
            rectangle(D2X,D2Y,0.075,0.25,255, 424, 186);
    }
    glEnd();
    // 球球
    int n = 100;
    GLfloat R = 0.03f;
    GLfloat Pi = 3.1415926536f;
    glBegin(GL_POLYGON);
    {
        glColor3ub(196, 69, 54);
        

        // 還沒開始遊戲
        if(StartGame == false)
        {
            BX = DX + 0.12f;
            BY = DY + 0.11f;
            for(int i=0; i<n; ++i)
                glVertex2f(BX+ R*cos(2*Pi/n*i) ,BY+ R*sin(2*Pi/n*i));
        }

        // 遊戲開始
        if(StartGame)
        {
            if(BX > 1.0f)
                xPath = -1;
            if(BX < -1.0f)
                xPath = 1;
            BX += (0.01f * xPath);

            if(BY > 1.0f)
                yPath = -1;
            if(BY < -1.0f)
                yPath = 1;
            BY += (0.01f * yPath);

             for(int i=0; i<n; ++i)
                glVertex2f(BX+ R*cos(2*Pi/n*i),BY +R*sin(2*Pi/n*i));
        }


        

            
    }
    glEnd();

    // 生命提示
    if(heart >= 1)
    {
        glBegin(GL_POLYGON);
        {
            glColor3ub(255, 0, 0);
            for(int i=0; i<n; ++i)
                glVertex2f(0.92f + R*cos(2*Pi/n*i),-0.92f+R*sin(2*Pi/n*i));
        }
        glEnd();
    }
    if(heart >= 2)
    {
        glBegin(GL_POLYGON);
        {
            glColor3ub(255, 0, 0);
            for(int i=0; i<n; ++i)
                glVertex2f(0.92f -0.09f + R*cos(2*Pi/n*i),-0.92f+R*sin(2*Pi/n*i));
        }
        glEnd();
    }
    if(heart >= 3)
    {
        glBegin(GL_POLYGON);
        {
            glColor3ub(255, 0, 0);
            for(int i=0; i<n; ++i)
                glVertex2f(0.92f -0.18f+ R*cos(2*Pi/n*i),-0.92f+R*sin(2*Pi/n*i));
        }
        glEnd();
    }
            
}

void BoolHit()
{
    // 撞擊下方
    for(int i=0 ; i<col*row ; i++)
    {
        if(BX >= RectX[i] && BX <= RectX[i]+0.25f && BY >= RectY[i] && BY <= RectY[i]+0.075f && RectShow[i])
        {
            RectShow[i] = 0;
            DistoryRectNumber += 1;

            // 球往左上移動(只會撞擊 方塊的 右方、下方)
            if(xPath == -1 && yPath == 1)
            {
                double left,down;
                left = BX - RectX[i];
                down = BY - RectY[i];

                if(left < down) // 先撞擊左方
                {
                    xPath = -xPath;
                }
                else if(left > down) // 相撞擊下方
                {
                    yPath = -yPath;
                }
                else
                {
                    xPath = -xPath;
                    yPath = -yPath;
                }
            }
            // 球往右上移動(只會撞擊 方塊的 左方、下方)
            else if(xPath == 1 && yPath == 1)
            {
                double right,down;
                right = RectX[i] + 0.25f - BX  ;
                down = BX - RectY[i];

                if(right < down) // 先撞擊左方
                {
                    xPath = -xPath;
                }
                else if(right > down) // 相撞擊下方
                {
                    yPath = -yPath;
                }
                else
                {
                    xPath = -xPath;
                    yPath = -yPath;
                }
            }

            // 球往左下移動(只會撞擊 方塊的 右方、上方)
            else  if(xPath == -1 && yPath == -1)
            {
                double left,up;
                left = RectX[i] + 0.25f - BX  ;
                up = RectY[i] + 0.125f - BY;

                if(left < up) // 先撞擊左方
                {
                    xPath = -xPath;
                }
                else if(left > up) // 相撞擊下方
                {
                    yPath = -yPath;
                }
                else
                {
                    xPath = -xPath;
                    yPath = -yPath;
                }
            }

            // 球往右下移動(只會撞擊 方塊的 左方、上方)
            else if(xPath == 1 && yPath == -1)
            {
                double right,up;
                right = BX - RectX[i]  ;
                up = RectY[i] + 0.125f - BY;

                if(right < up) // 先撞擊左方
                {
                    xPath = -xPath;
                }
                else if(right > up) // 相撞擊下方
                {
                    yPath = -yPath;
                }
                else
                {
                    xPath = -xPath;
                    yPath = -yPath;
                }
            }
        }
    }

    // 撞擊移動的桿子 easy
    if(BX >= DX && BX <= DX+0.25f && BY <= DY+0.075f)
    {
        BY = DY+0.075f;
        yPath = -yPath;
    }

    if(BY <= DY)
    {
        heart -= 1;
        StartGame = false;
    }


    // hard
    if(Level == 2)
    {
        if(BY >= D2Y && BY <= D2Y+0.25f && BX >= D2X)
        {
            BX = D2X;
            xPath = -xPath;
        }

        if(BX >= D2X+0.075f)
        {
            heart -= 1;
            StartGame = false;
        }
    }
}


int main(void)
{
    onInit();
    CreateRectangle();
    //
    while (!glfwWindowShouldClose(window))
    {
        KeyBoardInput(window);

        onResize();
        onUpdate();
        onRender();
        // 球的撞擊
        BoolHit();

        if(DistoryRectNumber == num )
        {
            if(Level == 3)
            {
                for(int i=0 ; i<num ; i++)
                    RectShow[i] = 0;
            }
            else if(Level == 2)
            {
                StartGame = false;
                Level = 3;
            }
            else if(Level == 1)
            {
                StartGame = false;
                Level = 2;
                DistoryRectNumber = 0;
                for(int i=0 ; i<42 ; i++)
                {
                    RectShow[i] = 1;
                }
                heart = 3;
            }
        }

        if(heart == 0)
        {
            StartGame = false;
            printf("end Game\n");
        }
        glfwSwapBuffers(window);
        glfwPollEvents();
    }

    glfwDestroyWindow(window);

    glfwTerminate();
    exit(EXIT_SUCCESS);
}
