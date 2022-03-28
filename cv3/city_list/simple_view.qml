import QtQuick 2.14
import QtQuick.Controls 2.14

Rectangle {
    width: 500
    height: 500

    Row {
        width: 500
        height: 500

        ListView {
            id: cityListView
            width: 250
            height: parent.height
            model: cityListModel

            Component {
                id: cityListDelegate
                Item {
                    height: childrenRect.height
                    width: parent.width

                    Text {
                        text: index + ':' + model.display
                        anchors.left : parent.left
                        anchors.right : parent.right    
                    }
                    MouseArea {
                        onClicked: cityListView.currentIndex = index
                        anchors.fill: parent
                    }
                }
            }

            delegate: cityListDelegate

            highlight: Rectangle {
                color: "red"
            }
        }

        Column {
            Text {
                text: "Rozloha:"
            }
            Text {
                text: "km2"
            }
            Text {
                text: "Počet obyvatel:"
            }
            Text {
                text: "obyv."
            }
        }
    }

}