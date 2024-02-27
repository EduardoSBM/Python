import React from 'react';
import { View, Text, StyleSheet, Image , SafeAreaView} from 'react-native';

function Teste() {
  return (
    <View style={styles.img}>
      <Image 
        style={styles.imagem}
        source={{ uri: 'https://scontent.fjjg4-1.fna.fbcdn.net/v/t39.30808-6/302569261_520520800074040_2275390801587503435_n.jpg?_nc_cat=111&ccb=1-7&_nc_sid=efb6e6&_nc_ohc=iiZaAOrsYEoAX-OYb4D&_nc_ht=scontent.fjjg4-1.fna&oh=00_AfCF2QbEWbm8mdy2aZRQCP6U9V9ert5vy9HWa-sacqHxWA&oe=65DCEDE0' }}
      />
      <Text style={styles.txt} >ooooo</Text> {/*criar view ou function para o txt*/ }
    </View>
  );
}

function Teste2() {
  return (
    <View>
      <Text>ooooo</Text>
    </View>
  );
}

export default function Home() {
  return (
    <SafeAreaView style={styles.container}>
      {/*<View style={styles.minhaLinha} />*/}
        <Teste/>

    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    //flex: 1,
    backgroundColor: 'white',
  
  },
  img:{
    justifyContent:'center',
    alignItems: 'flex-start',
    padding: '7%'
  },

  imagem: {
    height: 60,
    width: 60,
    borderRadius: 150,
    borderWidth: 2,
    borderColor: 'black',
 

    
  },
  minhaLinha: {
    position: 'absolute',
    top: 0,
    left: 0,
    width: '100%',
    height: '10%',
    backgroundColor: 'red',
    marginBottom: 10,
  },
});